"""
    This script contains functions and classes
    for the different sensitive APIs.
"""
import os
import sys
import re
import time
import logging
import threading
import jd_meta as jd_meta_func
from db_return import db_return
from db_no_return import db_no_return
from dotenv import load_dotenv
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
file_handler = logging.FileHandler(os.path.join(log_directory, "sensitive.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


# CAUTION : the python script and .env file
# need to be in the same path for below line.
dotenv_path = os.path.join(os.getcwd(), ".env")
# below dotenv_path for local test in Downloads folder
# dotenv_path = os.path.join(os.path.expanduser("~"), "Downloads", ".env")
load_dotenv(dotenv_path)


class Sensitive():
    """
        This class contains functions for the
        different sensitive APIs.
    """

    def tables(self):
        try:
            query = """SELECT table_name
                        FROM information_schema.tables
                        WHERE table_schema = 'public'
                        AND table_type = 'BASE TABLE';
                    """
            query_data = (None,)
            table_data = db_return(query, query_data)
            ret_data = []
            if table_data:
                ret_data = [element[0] for element in table_data]

            return {"fetch": True,
                    "tables_names": ret_data}, 200

        except Exception as view_list_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                    "fetch": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{view_list_error}",    # pylint: disable=line-too-long
                }, 500


    def table_data(self, table_name):
        try:
            query = f"""SELECT column_name
                    FROM information_schema.columns
                    WHERE table_name = %s
                    ORDER BY ordinal_position;
                    """
            query_data = (table_name,)
            column_data = db_return(query, query_data)
            column_data = [element[0] for element in column_data]
            query = f"""select * from {table_name};
                        """
            query_data = (None,)
            table_data = db_return(query, query_data)
            ret_data = []
            for element in table_data:
                temp_dct = {}
                for serial, col_name in enumerate(column_data):
                    temp_dct[col_name] = element[serial]
                ret_data.append(temp_dct)

            return {"fetch": True,
                    "data": ret_data}, 200

        except Exception as view_list_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                    "fetch": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{view_list_error}",    # pylint: disable=line-too-long
                }, 500
