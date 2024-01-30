"""
   this code contains the "READ" operation funtion(s) to connect
   python code to PostgreSQL database using pysycopg2
"""
import os
import sys
import logging
import psycopg2
from dotenv import load_dotenv


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
file_handler = logging.FileHandler(os.path.join(log_directory, "db_return.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


# CAUTION : the python script and .env file need
# to be in the same path for below line.
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
except Exception as env_error:  # pylint: disable=broad-exception-caught
    logger.critical("Failed to read DB params: %s", env_error)
    sys.exit()


def db_return(query, query_data):
    """Function that executes (a) query (queries) and
       return(s) some data from the database
    """

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

    except Exception as db_error:   # pylint: disable=broad-exception-caught
        exception_type, _, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno
        logger.error("%s||||%s||||%s", exception_type, filename, line_number)
        return {
            "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
        }

    # except Error as e:
    #     logger.error(f"Error: {e}")

    finally:
        # Close the cursor and the database connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
