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
import time
from datetime import datetime, timedelta
from decimal import Decimal#, getcontext
import pandas as pd
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


class DecimalEncoder(json.JSONEncoder):
    """this class is to convert Decimal datatypes to float"""
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super().default(o)


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
                        prompt, model_params, tokens, cost, timestamp)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""]

        query_data = [(
                        req_body["challenge_id"],
                        req_body["gen_ai_api"],
                        json.dumps(req_body["input"]),
                        json.dumps(req_body["output"]),
                        req_body["prompt"],
                        req_body["modelParams"],
                        req_body["tokens"],
                        req_body["cost"],
                        time.time()
                        )]

        try:
            res = db_no_return(queries_list, query_data)

            if  res == "success":   # pylint: disable=no-else-return
                threading.Thread(target=update_total_usage, args=(
                        req_body["challenge_id"],
                        req_body["tokens"],
                        req_body["cost"],
                        req_body["gen_ai_api"]
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


def update_total_usage(challenge_id, tokens, cost, gen_ai_api):
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
    if gen_ai_api != "/gen_ai_api/generate_solution":
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
    else:
        query = [
                """INSERT INTO gen_ai_token_usage (challenge_id, tokens, cost, ai_tokens, ai_cost)
                   VALUES (%s, %s, %s, %s, %s)
                   ON CONFLICT (challenge_id) DO UPDATE 
                   SET tokens = gen_ai_token_usage.tokens + %s,
                       cost = gen_ai_token_usage.cost + %s,
                       ai_tokens = %s,
                       ai_cost = %s;"""
            ]
        query_data = [
                        (
                            challenge_id,
                            tokens,
                            cost,
                            tokens,
                            cost,
                            tokens,
                            cost,
                            tokens,
                            cost,
                        ),
                    ]
    db_no_return(query, query_data)


# def fetch_gen_usage(req_body):
#     """this function fetches the tokens and cost incurred for a particular challenge_id"""

#     try:
#         query = "select tokens,cost from gen_ai_token_usage where challenge_id=%s"
#         query_data = (req_body["challenge_id"],)
#         res = db_return(query, query_data)
#         if res:    # pylint: disable=no-else-return
#             return {"tokens": res[0][0],
#                     "cost": str(res[0][1]),
#                     "fetch": True}, 200
#         else:
#             return {"fetch": False,
#                     "helpText":"no records found"}, 400

#     except Exception as db_error:  # pylint: disable=broad-exception-caught
#         exception_type, _, exception_traceback = sys.exc_info()
#         filename = exception_traceback.tb_frame.f_code.co_filename
#         line_number = exception_traceback.tb_lineno
#         logger.error("%s||||%s||||%d", exception_type, filename, line_number)
#         return {
#             "fetch": False,
#             "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
#         }, 500


def fetch_gen_usage_user_wise(req_body):  # pylint: disable=too-many-locals,too-many-statements
    """this function fetches the tokens and cost incurred for challenges user-wise"""

    try:
        query = """SELECT
                        CONCAT(us.f_name, ' ', us.l_name) AS name,
                        us.employee_id,
                        SUM(COALESCE(gu.tokens, 0)) AS total_tokens,
                        SUM(COALESCE(gu.ai_tokens, 0)) AS total_ai_tokens,
                        SUM(COALESCE(gu.cost, 0)) AS total_cost,
                        SUM(COALESCE(gu.ai_cost, 0)) AS total_ai_cost,
                        SUM(COALESCE(gu.tokens, 0)) - SUM(COALESCE(gu.ai_tokens, 0)) AS user_tokens,
                        SUM(COALESCE(gu.cost, 0)) - SUM(COALESCE(gu.ai_cost, 0)) AS user_cost
                    FROM
                        gen_ai_token_usage gu
                    LEFT JOIN
                        challenge c ON gu.challenge_id = c.challenge_id
                    LEFT JOIN
                        user_signup us ON c.initiator_id = us.email
                    GROUP BY
                        CONCAT(us.f_name, ' ', us.l_name),
                        us.employee_id;
                """
        query_data = None
        query1 = """SELECT gaa.challenge_id, gaa.gen_ai_api, gaa.cost, gaa.tokens, gaa.timestamp, CONCAT(us.f_name, ' ', us.l_name) AS name, us.employee_id
                    FROM gen_ai_analytics gaa
                    LEFT JOIN challenge c
                    ON gaa.challenge_id = c.challenge_id
                    LEFT JOIN user_signup us
                    ON us.email = c.initiator_id
                    WHERE gaa.timestamp >= %s
                    AND gaa.timestamp <= %s;"""
        query_data1 = (req_body['start_epoch'], req_body['end_epoch'])
        res1 = db_return(query1, query_data1)
        res = db_return(query, query_data)
        # print (res,"\n\n\n\n")
        # print (res1,"\n\n\n\n")
        ai_df = pd.DataFrame()
        u_df = pd.DataFrame()
        if res1:
            df = pd.DataFrame(res1, columns=["challenge_id", "gen_ai_api", "cost", "tokens", "timestamp", "name", "employee_id"])  # pylint: disable=invalid-name
            # print(df)
            condition = df['gen_ai_api'] == '/gen_ai_api/generate_solution'
            ai_df = df[condition]
            u_df = df[~condition]
            # print(ai_df)
            # print(u_df)
            u_df.loc[:, 'timestamp'] = pd.to_datetime(u_df['timestamp'], unit='s')

            # Filter records from the last 12 months
            current_date = datetime.now()
            last_12_months = current_date - timedelta(days=365)
            filtered_df = u_df[u_df['timestamp'] >= last_12_months]

            # Group by 'name', 'year', and 'month' and calculate total cost and total tokens
            grouped_df = filtered_df.rename(columns={'timestamp': 'date'}).groupby(['employee_id', filtered_df['timestamp'].dt.year.rename('year'), filtered_df['timestamp'].dt.month_name().rename('month')]).agg({'cost': 'sum', 'tokens': 'sum'}).reset_index()

            # Convert the 'cost' column to string format
            grouped_df['cost'] = grouped_df['cost'].astype(str)

            # Convert the grouped DataFrame to a nested dictionary with "month-year" as keys
            result_dict = {}
            for _, row in grouped_df.iterrows():
                # name = row['name']
                year = row['year']
                month = row['month']
                cost = row['cost']
                tokens = row['tokens']
                employee_id = row['employee_id']

                if employee_id not in result_dict:
                    result_dict[employee_id] = {}

                if f"{month}-{year}" not in result_dict[employee_id]:
                    result_dict[employee_id][f"{month}-{year}"] = {'cost': cost, 'tokens': tokens}

        if not ai_df.empty:
            ai_df = ai_df[["cost", "tokens", "timestamp"]]
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

            # Extract year and month from timestamp
            df['year'] = df['timestamp'].dt.year
            df['month'] = df['timestamp'].dt.month_name()

            # Group by 'year' and 'month' and calculate total cost and tokens for each month-year
            grouped_df = df.groupby(['year', 'month']).agg({'cost': 'sum', 'tokens': 'sum'}).reset_index()

            # Convert the 'cost' column to string format
            grouped_df['cost'] = grouped_df['cost'].astype(str)

            # Convert the grouped DataFrame to a dictionary with "month-year" as keys
            ai_result_dict = grouped_df.set_index(['month', 'year']).to_dict(orient='index')

        data2 = None
        if res1:
            if ai_df.empty:
                data2 = {"user_data": result_dict,
                         "ai_data": None}
            else:
                ai_result_dict_str = {str(k): v for k, v in ai_result_dict.items()}  # Convert keys to strings
                converted_data = {key[1:-1].replace("', ", "-").replace("'", ""): value for key, value in ai_result_dict_str.items()}
                data2 = {"user_data": result_dict, "ai_data": converted_data}
        if res:    # pylint: disable=no-else-return
            converted_list = [
                        (name, employee_id, num1, num2, str(num3), str(num4), num5, str(num6))
                        for name, employee_id, num1, num2, num3, num4, num5, num6 in res
                    ]
            return {"fetch": True,
                    "data1": converted_list,
                    "data2": data2,
                    "fields1": ["user_name","employee_id","total_tokens","total_ai_tokens","total_cost","total_ai_cost","user_tokens","user_cost"]}, 200
        else:
            return {"fetch": False,
                    "data1": None,
                    "data2": data2,
                    "helpText":"no records found"}, 400

    except Exception as db_error:  # pylint: disable=broad-exception-caught
        exception_type, _, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno
        logger.error("%s||||%s||||%d", exception_type, filename, line_number)
        return {
            "fetch": False,
            "data1": None,
            "data2": None,
            "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
        }, 500
