"""
    this code contains function to fetch data for
    "Setting Parameters" tab's key parameters
"""
import sys
import logging
from db_return import db_return
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
