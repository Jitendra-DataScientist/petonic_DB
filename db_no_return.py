"""
   this code contains the "CREATE" or "UPDATE" operation funtion(s)
   to connect python code to PostgreSQL database using pysycopg2
"""
import os
import sys
import logging
import psycopg2
from dotenv import load_dotenv


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

# Create a logger instance
logger = logging.getLogger(__name__)


# CAUTION : the python script and .env file
# need to be in the same path for below line.
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


def db_no_return(queries_list, query_data):
    """function for processing (a) query (queries) that
       do(does) not return any response(s) from database"""
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(**db_params)

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        try:
            for query_count, query in enumerate(queries_list):
                # Execute the query
                cursor.execute(query, query_data[query_count])

                # Print a success message
                logger.info("Query %d executed successfully", query_count)

            # Commit the transaction
            connection.commit()

            return "success"

        except psycopg2.errors.UniqueViolation:     # pylint: disable=no-member
            return {
                "helpText": "Primary-key Violation Error",
            }

        except psycopg2.errors.ForeignKeyViolation:     # pylint: disable=no-member
            return {
                "helpText": "Foreign-key Violation Error",
            }

        except Exception as db_error:     # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",     # pylint: disable=line-too-long
            }

    except Exception as db_error:     # pylint: disable=broad-exception-caught
        exception_type, _, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno
        logger.error("%s||||%s||||%d", exception_type, filename, line_number)
        return {
            "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",
        }

    finally:
        # Close the cursor and the database connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
