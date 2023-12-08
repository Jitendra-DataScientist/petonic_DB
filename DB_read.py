# pylint: disable=too-many-lines
"""
    this code primarily contains the funtions to connect
    python code to PostgreSQL database using pysycopg2
"""
import os
import sys
import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import json
import logging
import pandas as pd
import psycopg2
from psycopg2 import Error
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

# Create a logger instance
logger = logging.getLogger(__name__)


# CAUTION : the python script and .env file need to be in the same path for below line.
dotenv_path = os.path.join(os.getcwd(), ".env")
# below dotenv_path for local test in Downloads folder
# dotenv_path = os.path.join(os.path.expanduser("~"), "Downloads", ".env")
load_dotenv(dotenv_path)

# Database connection parameters
try:
    db_params = {
        "host": os.getenv("host"),
        "database": os.getenv("database"),
        "user": os.getenv("user"),
        "password": os.getenv("password"),
    }
except Error as env_error:
    logger.critical("Failed to read DB params: %s", env_error)
    sys.exit()


class DB_read:
    def db_read(self, query, query_data):   # pylint: disable=too-many-branches
        """Function that executes (a) query (queries) and return(s) some data from the database"""

        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Execute the query
            if query_data:
                cursor.execute(query, query_data)
            else:
                cursor.execute(query)

            return cursor.fetchall()

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"
            }

        # except Error as e:
        #     logger.error(f"Error: {e}")

        finally:
            # Close the cursor and the database connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()