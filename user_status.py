"""
This code contains the function to activate
and deactivate a particular user profile on
User Management Page (to be done by the admin).
"""
import sys
import logging
from db_read import db_read
from db_create_update import db_create_update
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


def flip_user_status(req_body):
    """
        function to deactivate or reactivate
        a particular user profile on User
        Management Page (to be done by
        admin).
    """
    try:
        # Queries Formation
        queries_list = ["UPDATE validation\
                        SET active = NOT active\
                        WHERE email = %s;",]

        query_data = [(req_body["email"],),]

        try:
            res = db_create_update(queries_list, query_data)

            if  res == "success":   # pylint: disable=no-else-return
                return {"update": True}, 200
            else:
                res.update({"update": False})
                return res, 400

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                "update": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 400

    except Exception as db_error:  # pylint: disable=broad-exception-caught
        exception_type, _, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno
        logger.error("%s||||%s||||%d", exception_type, filename, line_number)
        return {
            "update": False,
            "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
        }, 500
