"""
    this code contains function to fetch data
    for "Setting Parameters" tab's key factors
"""
import sys
import logging
from db_read import db_read
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


def setting_parameter_key_factors(req_body):
    """function to fetch data for "Setting Parameters"
       tab's key factors
    """

    try:
        query = "select key_factor, suggested_values, description\
                from industry_domain_process_key_factors\
                where industry = %s\
                and domain = %s\
                and process = %s;"
        query_data = (req_body["industry"],
                      req_body["domain"],
                      req_body["process"],)

        return db_read(query, query_data)

    except Exception as db_error:  # pylint: disable=broad-exception-caught
        exception_type, _, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno
        logger.error("%s||||%s||||%s", exception_type, filename, line_number)
        return {
            "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
        }
