"""
    This code contains the Demo class that has methods
    for the "Request Demo" features of the product.
"""
import os
import sys
import logging
from db_no_return import db_no_return


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
file_handler = logging.FileHandler(os.path.join(log_directory, "demo.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)



class Demo:
    """
        The Demo class that has methods for the
        "Request Demo" features of the product.
    """

    def solvai_demo(self, req_body):  # pylint: disable=too-many-locals
        """Function to insert data into the solvai_demo table."""
        try:
            # Queries Formation
            query = ["""INSERT INTO solvai_demo
                     (email, name, company_name, details)
                     VALUES (%s, %s,%s,%s);""",]
            query_data = [
                            (
                                req_body["email"],
                                req_body["name"],
                                req_body["company_name"],
                                req_body["details"],
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
