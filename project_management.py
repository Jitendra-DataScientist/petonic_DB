"""
    this code primarily contains the functions that
    are project management related
"""
import os
import sys
# from bson import json_util
# from pymongo import json_util
import logging
from db_return import db_return
from db_no_return import db_no_return
from challenge_generic import CG


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
file_handler = logging.FileHandler(os.path.join(log_directory, "project_management.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


challenge_generic_instance = CG()

class PM:   # pylint: disable=too-few-public-methods
    """
       this class primarily contains the functions that
       are project management related
    """
    def project_initiation(self, req_Body):
        """ function to add project manager name and
            project management tool eing used, to DB
        """
        try:
            req_body = req_Body.copy()
            req_body['pm_id'] = req_body['pm_id'].lower()
            # check if the challenge_id is present in challenge table
            challenge_check = challenge_generic_instance.challenge_count(
                {"challenge_id": req_body["challenge_id"]}
                )[0]['count']

            if challenge_check == 0:
                return {
                        "update": False,
                        "helpText": "Invalid challenge_id"
                    }, 400

            # check if the pm_id and pm_tool already assigned
            query = "SELECT pm_id, pm_tool\
                    FROM challenge\
                    WHERE challenge_id = %s;"
            query_data = (
                            req_body["challenge_id"],
                        )

            pm_check = db_return(query, query_data)
            if pm_check[0][0] and pm_check[0][1]:
                return {
                        "update": False,
                        "helpText": "pm_id & pm_tool already assigned"
                    }, 400

            # Queries Formation
            query = ["UPDATE challenge SET pm_id = %s, pm_tool = %s WHERE challenge_id = %s;",]
            query_data = [
                            (
                                req_body["pm_id"],
                                req_body["pm_tool"],
                                req_body["challenge_id"],
                            ),
                        ]

            try:
                res = db_no_return(query, query_data)

                if res == "success":   # pylint: disable=no-else-return
                    return {"update": True}, 201
                else:
                    # logger.warning("challenge_id already present")
                    res.update({"update": False})
                    return res, 400

            except Exception as db_error:  # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)    # pylint: disable=line-too-long
                return {
                    "update": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "update": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500
