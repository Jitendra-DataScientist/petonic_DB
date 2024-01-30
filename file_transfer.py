"""
    this code is primarily related to file transfers
"""
import os
import sys
import time
import logging
from fastapi.responses import FileResponse
from utils import Utils


current_dir = os.getcwd()
print("Current Directory: %s", current_dir)

current_dir_split = current_dir.split('\\')
if current_dir_split[-1] != 'files':
    try:
        if current_dir_split[-2] == 'files':
            log_dir = current_dir + '/../..'
        else:
            log_dir = current_dir
    except IndexError:
        log_dir = current_dir
else:
    log_dir = current_dir + '/..'

log_dir = os.path.join(log_dir, 'logs')

if not os.path.exists(log_dir):
    os.mkdir(log_dir)

# Configure logging
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     handlers=[logging.StreamHandler()],
# )

# Create a logger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler for this script's log file
file_handler = logging.FileHandler(os.path.join(log_dir, "file_transfer.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


utils = Utils()


class FT:
    """
       this class has funtions primarily related to file transfers
    """

    def file_upload(self, path_key, files):
        """function for uploading file(s)"""
        try:
            # path_key to be of form "challenge-id _ contributor-id _ solution-id _ epoch"
            current_directory = os.getcwd()
            logger.info("Current Directory: %s", current_directory)

            new_directory = os.path.join(current_directory, 'files')

            if not os.path.exists(new_directory):
                os.mkdir(new_directory)
                logger.info("The directory '%s' created.", new_directory)

            new_directory = os.path.join(new_directory, f'{path_key}_{time.time()}')

            try:
                os.mkdir(new_directory)
            except FileExistsError:
                return {"upload": False, "message": "path_key already exists"}, 400

            try:
                for file in files:
                    try:
                        file_path = os.path.join(new_directory, file.filename)
                        with open(file_path, 'wb') as file_obj:
                            file_obj.write(file.file.read())
                    except Exception:  # pylint: disable=broad-exception-caught
                        return {"message": "There was an error uploading the file(s)"}, 500
                    finally:
                        file.file.close()

                return {"upload": True,
                        "message": f"Successfully uploaded {[file.filename for file in files]}"
                        }, 200

            except Exception as file_error:  # pylint: disable=broad-exception-caught
                return {"upload": False, "helpText": file_error}, 500

        except Exception as upload_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type,
                         filename, line_number, upload_error)
            return {
                "upload": False,
                "helpText": f"Exception: {exception_type}||||{filename}\
                    ||||{line_number}||||{upload_error}",
            }, 500


    def file_download(self, payload):
        """function for downloading a file"""
        try:
            path_key = payload.get("path_key")
            filename = payload.get("filename")

            if not path_key or not filename:
                return {"helpText": "Both path_key and filename are required in the payload."}, 400

            current_directory = os.getcwd()
            files_directory = os.path.join(current_directory, 'files', path_key)
            file_path = os.path.join(files_directory, filename)

            try:
                if os.path.exists(files_directory):
                    if os.path.exists(file_path):   # pylint: disable=no-else-return
                        return FileResponse(file_path, filename=filename,
                                            media_type="application/octet-stream"), 200
                    else:
                        return {"helpText": f"{filename} file not found at path_key: \
                                {path_key}"}, 404
                else:
                    return {"helpText": f"{path_key} path_key not found."}, 404
            except Exception as download_error:   # pylint: disable=broad-exception-caught
                return {"helpText": f"An error occurred while processing\
                        the request: {str(download_error)}"}, 500

        except Exception as download_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type,
                         filename, line_number, download_error)
            return {
                "upload": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||\
                    {line_number}||||{download_error}",
            }, 500


    def get_epoch_from_folder_name(self, folder_name):
        """function used in get_folder_contents function to extract epoch from folder names"""
        return float(folder_name.rsplit("_", 1)[-1])


    def get_folder_contents(self, directory, prefix=""):
        """function to get the folder and then files within them,
           in a particular path prefix inside given directory
        """
        try:
            folder_contents = {}
            sorted_folder_contents = {}
            try:
                list_dir = os.listdir(directory)
            except FileNotFoundError:
                return {"list_fetch": False,
                    "helpText": "folder 'files' not yet created."}
            for folder in list_dir:
                folder_path = os.path.join(directory, folder)
                if os.path.isdir(folder_path) and folder.startswith(prefix):
                    contents = os.listdir(folder_path)
                    folder_contents[folder] = contents
            if folder_contents:
                sorted_folder_contents = dict(sorted(folder_contents.items(),
                                     key=lambda item: self.get_epoch_from_folder_name(item[0]),
                                     reverse=True))

            return {"list_fetch": True,
                    "folder_structure": sorted_folder_contents}
        except Exception as view_list_error:  # pylint: disable=broad-exception-caught
            logger.error("An error occurred: %s", str(view_list_error))
            return {"list_fetch": False,
                    "helpText": str(view_list_error)}


    def view_file_list(self, payload):
        """function to trigger get_folder_contents with appropriate directory and prefix"""
        try:
            current_directory = os.getcwd()
            logger.info("Current Directory: %s", current_directory)

            files_directory = os.path.join(current_directory, 'files')
            return self.get_folder_contents(files_directory, payload['path_key_prefix']), 200

        except Exception as fetch_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, fetch_error)
            return {
                "list_fetch": False,
                "helpText": f"Exception: {exception_type}||||\
                {filename}||||{line_number}||||{fetch_error}",
            }, 500
