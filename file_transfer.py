"""
    this code is primarily related to file transfers
"""
import os
import sys
import time
import logging
from fastapi.responses import FileResponse
from psycopg2 import Error
from utils import Utils

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

# Create a logger instance
logger = logging.getLogger(__name__)


utils = Utils()


class FT:
    """
       this class has funtions primarily related to file transfers
    """
    def file_upload(self, path_key, files):  # pylint: disable=too-many-locals
        """function for uploading file(s)"""
        try:
            # path_key to be of form "challenge-id _ contributor-id _ solution-id _ epoch"
            current_directory = os.getcwd()
            print(f"Current Directory: {current_directory}")

            current_directory_split = current_directory.split('\\')
            if current_directory_split[-1] != 'files':
                new_directory = current_directory + '/files'
                print (new_directory)
                if os.path.exists(new_directory):
                    os.chdir(new_directory)
                    print(f"The directory '{new_directory}' exists.")
                else:
                    os.mkdir(new_directory)
                    os.chdir(new_directory)
                    print(f"The directory '{new_directory}' exists.")

                new_directory = new_directory + '/' + path_key + '_' + str(time.time())
            else:
                new_directory = current_directory + '/' + path_key + '_' + str(time.time())

            try:
                os.mkdir(new_directory)
            except FileExistsError:
                return {"upload":False,
                        "message": "path_key already exists"}, 400

            os.chdir(new_directory)

            # Verify the change
            updated_directory = os.getcwd()
            print("Updated Working Directory:", updated_directory)

            try:
                for file in files:
                    try:
                        contents = file.file.read()
                        with open(file.filename, 'wb') as file_obj:
                            file_obj.write(contents)
                    except Exception:  # pylint: disable=broad-exception-caught
                        return {"message": "There was an error uploading the file(s)"}, 500
                    finally:
                        file.file.close()

                new_directory = updated_directory + '/../..'
                os.chdir(new_directory)

                return {"upload": True,
                        "message":
                        f"Successfully uploaded {[file.filename for file in files]}"
                        }, 200

            except Error as file_error:
                new_directory = updated_directory + '/../..'
                os.chdir(new_directory)
                return {"upload":False,
                        "error": file_error}, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "upload": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
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
                # import os
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

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "upload": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||\
                    {line_number}||||{db_error}",
            }, 500
