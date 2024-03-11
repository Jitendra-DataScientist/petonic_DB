"""
    this code primarily contains the funtions for
    wrting the GenAI APIs' inputs, outputs, human
    feedback etc. into the DB
"""
import os
import json
import sys
import logging
# from decimal import Decimal, getcontext
from db_no_return import db_no_return
from utils import Utils

# # Set the precision and scale for Decimal objects
# getcontext().prec = 9


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
file_handler = logging.FileHandler(os.path.join(log_directory, "gen_ai_analytics.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


utils = Utils()


# class GenAnalytics:
#     """
#         this class primarily contains the funtions for
#         wrting the GenAI APIs' inputs, outputs, human
#         feedback etc. into the DB
#     """


def gen_res_write(req_body):
    """function to write response of Gen AI API into
        DB, specifically, challenge_id, gen_ai_api, input,
        output, prompt and model_params, into the DB
    """
    try:
        # Queries Formation
        queries_list = ["""INSERT INTO gen_ai_analytics
                        (challenge_id, gen_ai_api, input, output,
                        prompt, model_params, tokens, cost)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""]

        query_data = [(req_body["challenge_id"],
                        req_body["gen_ai_api"],
                        json.dumps(req_body["input"]),
                        json.dumps(req_body["output"]),
                        req_body["prompt"],
                        json.dumps(req_body["modelParams"]),
                        req_body["tokens"],
                        req_body["cost"],
                        )]

        try:
            res = db_no_return(queries_list, query_data)

            if  res == "success":   # pylint: disable=no-else-return
                return {"update": True}, 201
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
