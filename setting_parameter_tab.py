"""
    this code contains function to fetch data for
    "Setting Parameters" tab's key parameters
"""
import os
import sys
import logging
from db_return import db_return
from utils import Utils


# Determine the directory for logs
log_directory = os.path.join(os.getcwd(), 'logs')

# Create the logs directory if it doesn't exist
if not os.path.exists(log_directory):
    os.mkdir(log_directory)

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
file_handler = logging.FileHandler(os.path.join(log_directory, "setting_parameter_tab.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


utils = Utils()


def setting_parameter_key_parameters(req_body):
    """function to fetch data for "Setting
       Parameters" tab's key parameters
    """

    try:
        query = "select key_parameter, suggested_values, description\
                from industry_domain_process_key_parameters\
                where industry_name = %s\
                and domain_name = %s\
                and process_name = %s;"
        query_data = (req_body["industry"],
                      req_body["domain"],
                      req_body["process"],)

        return db_return(query, query_data)

    except Exception as db_error:  # pylint: disable=broad-exception-caught
        exception_type, _, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno
        logger.error("%s||||%s||||%s", exception_type, filename, line_number)
        return {
            "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
        }
