"""
    this code primarily contains the funtions for
    wrting the GenAI APIs' inputs, outputs, human
    feedback etc. into the DB
"""
import os
import json
import sys
import logging
import threading
# from decimal import Decimal, getcontext
from db_no_return import db_no_return
from db_return import db_return
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
                threading.Thread(target=update_total_usage, args=(
                        req_body["challenge_id"],
                        req_body["tokens"],
                        req_body["cost"]
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


def update_total_usage(challenge_id, tokens, cost):
    """this function updates the gen_ai_token_usage
       table in the DB for a particular challenge_id
    """

    # query = """SELECT tokens,cost
    #            FROM gen_ai_analytics
    #            WHERE challenge_id=%s;"""
    # query_data = (challenge_id,)
    # res = db_return(query,query_data)
    # if res:
    #     res = [(0 if value is None else value, 0 if cost is None else \
    #            cost) for value, cost in res]
    #     tokens = sum(0 if token is None else token for token, _ in res)
    #     costs = sum(0 if cost is None else cost for _, cost in res)
    #     return res,tokens,costs
    query = [
            """INSERT INTO gen_ai_token_usage (challenge_id, tokens, cost)
                VALUES (%s, %s, %s)
                ON CONFLICT (challenge_id) DO UPDATE 
                SET tokens = gen_ai_token_usage.tokens + %s,
                    cost = gen_ai_token_usage.cost + %s;"""
        ]
    query_data = [
                    (
                        challenge_id,
                        tokens,
                        cost,
                        tokens,
                        cost,
                    ),
                ]

    db_no_return(query, query_data)


def fetch_gen_usage(challenge_id):
    """this function fetches the tokens and cost incurred for a particular challenge_id"""

    try:
        query = "select tokens,cost from gen_ai_token_usage where challenge_id=%s"
        query_data = (challenge_id,)
        res = db_return(query, query_data)
        if res:    # pylint: disable=no-else-return
            return {"tokens": res[0][0],
                    "cost": res[0][1],
                    "fetch": True}, 200
        else:
            return {"fetch": False,
                    "helpText":"no records found"}, 400

    except Exception as db_error:  # pylint: disable=broad-exception-caught
        exception_type, _, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno
        logger.error("%s||||%s||||%d", exception_type, filename, line_number)
        return {
            "update": False,
            "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
        }, 500
