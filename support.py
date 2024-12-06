"""
    This code contains the Support class that has
    methods for the support features of the product.
"""
import os
import sys
import logging
import time
import threading
from db_no_return import db_no_return
from utils import Utils
import json


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
file_handler = logging.FileHandler(os.path.join(log_directory, "support.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


utils_instance = Utils()


class Support:
    """
        The Support class that has methods for
        the support features of the product.
    """

    def solvai_support(self, req_body):  # pylint: disable=too-many-locals
        """Function to insert data into the solvai_support table."""
        try:
            # Queries Formation
            query = ["""INSERT INTO solvai_support
                     (email, name, query, subscription_id, API_hit_timestamp)
                     VALUES (%s,%s,%s,%s,%s);""",]
            query_data = [
                            (
                                req_body["email"],
                                req_body["name"],
                                req_body["query"],
                                req_body["subscription_id"],
                                time.time(),
                            ),
                        ]

            res = db_no_return(query, query_data)

            if res == "success":   # pylint: disable=no-else-return
                threading.Thread(
                    target=utils_instance.solvai_support, args=(
                                req_body["email"],
                                req_body["name"],
                                req_body["query"]
                                )
                    ).start()
                return {"update": True}, 201

            else:
                res.update({"update": False})
                return res, 400

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "update": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500


    def petonicai_support(self, req_body, table_name):  # pylint: disable=too-many-locals
        """Function to insert data into the petonicai_support / plannex_support table."""
        try:
            # Queries Formation
            if table_name == "plannex_support":
                query = [f"""INSERT INTO {table_name}
                        (email, first_name, last_name, service, company, query, API_hit_timestamp,json_data)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);""",]
                query_data = [
                                (
                                    req_body["email"],
                                    req_body["first_name"],
                                    req_body["last_name"],
                                    req_body["service"],
                                    req_body["company"],
                                    req_body["query"],
                                    time.time(),
                                    json.dumps(req_body["json_data"]),
                                ),
                            ]
            else:
                query = [f"""INSERT INTO {table_name}
                        (email, first_name, last_name, service, company, query, API_hit_timestamp)
                        VALUES (%s,%s,%s,%s,%s,%s,%s);""",]
                query_data = [
                                (
                                    req_body["email"],
                                    req_body["first_name"],
                                    req_body["last_name"],
                                    req_body["service"],
                                    req_body["company"],
                                    req_body["query"],
                                    time.time(),
                                ),
                            ]

            res = db_no_return(query, query_data)

            if res == "success":   # pylint: disable=no-else-return
                if table_name == "plannex_support":
                    threading.Thread(
                        target=utils_instance.support, args=(
                                    req_body["email"],
                                    req_body["first_name"],
                                    req_body["last_name"],
                                    req_body["service"],
                                    req_body["company"],
                                    req_body["query"],
                                    table_name,
                                    req_body["json_data"],
                                    )
                        ).start()
                    plannex_poc_email_ids = os.getenv("plannex_poc_mails")
                    plannex_poc_email_ids_list = plannex_poc_email_ids.split(",") if plannex_poc_email_ids else []
                    for plannex_poc_mail_id in plannex_poc_email_ids_list:
                        threading.Thread(
                            target=utils_instance.poc_support, args=(
                                        plannex_poc_mail_id,
                                        req_body["first_name"],
                                        req_body["last_name"],
                                        req_body["service"],
                                        req_body["company"],
                                        req_body["query"],
                                        req_body["json_data"],
                                        req_body["email"],
                                        )
                            ).start()
                else:
                    threading.Thread(
                        target=utils_instance.support, args=(
                                    req_body["email"],
                                    req_body["first_name"],
                                    req_body["last_name"],
                                    req_body["service"],
                                    req_body["company"],
                                    req_body["query"],
                                    table_name,
                                    )
                        ).start()
                return {"update": True}, 201

            else:
                res.update({"update": False})
                return res, 400

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "update": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500


    def plannex_contact_us(self, req_body):  # pylint: disable=too-many-locals
        """Function to insert data into the plannex_contact_us table."""
        try:
            # Queries Formation
            query = ["""INSERT INTO plannex_contact_us
                     (email, first_name, last_name, query, company, api_hit_timestamp, json_data)
                     VALUES (%s,%s,%s,%s,%s,%s,%s);""",]
            query_data = [
                            (
                                req_body["email"],
                                req_body["first_name"],
                                req_body["last_name"],
                                req_body["query"],
                                req_body["company"],
                                time.time(),
                                json.dumps(req_body["json_data"]),
                            ),
                        ]

            res = db_no_return(query, query_data)

            if res == "success":   # pylint: disable=no-else-return
                return {"update": True}, 201

            else:
                res.update({"update": False})
                return res, 400

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "update": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500
