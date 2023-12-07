"""
    this script hosts data-api routes
    that are written on FASTAPI
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
from DB_psycopg2 import DB_psycopg2


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

# Create a logger instance
logger = logging.getLogger(__name__)


# Create a FastAPI instance
app = FastAPI()


@app.get("/data-api/health")
async def health():
    """Route funtion to return health status of data-api"""

    return JSONResponse(content={"API_status": "healthy"}, status_code=200)


@app.post("/data-api/login")
async def data_api_login(payload: Request):
    """Route function for user login action"""

    req_body = await payload.json()
    login_DB_inst = DB_psycopg2()
    data = login_DB_inst.login(req_body)
    logger.info(data)
    # below 2 lines for testing
    # data[0] = ("qw",0)
    # data[0] = (12,0)
    if isinstance(data[0][0], int):
        if data[0][0] == 1:                             # pylint: disable=no-else-return
            return JSONResponse(content={"login": True}, status_code=200)
        elif data[0][0] == 0:
            return JSONResponse(content={"login": False}, status_code=401)
        else:
            return JSONResponse(
                content={"login": True, "IT_alert": True}, status_code=202
            )
    else:
        return JSONResponse(
            content={"helpText": {"data": data}, "login": False}, status_code=401
        )


@app.post("/data-api/signup")
async def data_api_signup(payload: Request):
    """Route function for user signup action"""

    req_body = await payload.json()
    signup_DB_inst = DB_psycopg2()
    signup_response, status_code = signup_DB_inst.signup(req_body)
    return JSONResponse(content=signup_response, status_code=status_code)


@app.post("/data-api/validation")
async def data_api_validation(payload: Request):
    """Route function for user validation action"""

    req_body = await payload.json()
    validation_DB_inst = DB_psycopg2()
    validation_response, status_code = validation_DB_inst.validation(req_body)
    return JSONResponse(content=validation_response, status_code=status_code)


@app.post("/data-api/forgot-password")
async def data_api_forgot_password(payload: Request):         # pylint: disable=too-many-return-statements
    """Route function for forgot-password action"""

    req_body = await payload.json()
    forgot_password_DB_inst = DB_psycopg2()
    data = forgot_password_DB_inst.forgot_password_response_from_query(req_body)
    logger.info(data)
    # below 2 lines for testing
    # data[0] = ("qw",0)
    # data[0] = (12,0)
    if isinstance(data[0][0], int):
        if data[0][0] == 1:
            reset_action = forgot_password_DB_inst.forgot_password_execute_query(req_body)
            if reset_action["reset"]:
                try:
                    logger.info(                 # pylint: disable=logging-too-many-args
                        "In function: ",
                        forgot_password_DB_inst.send_mail_trigger_forgot_pass(
                            req_body["email"], reset_action["new_password"]
                        ),
                    )
                    return JSONResponse(content={"reset_link": True}, status_code=201)
                except Error as mail_error3:
                    logger.error("Failed to send mail: %s", mail_error3)
                    return JSONResponse(
                        content={
                            "reset_link": False,
                            "helpText": "failed to send mail",
                        },
                        status_code=500,
                    )
            else:
                return JSONResponse(
                    content={
                        "reset_link": False,
                        "helpText": "failed to generate password",
                    },
                    status_code=500,
                )
        elif data[0][0] == 0:
            return JSONResponse(
                content={"reset_link": False, "uiText": "Unidentified email ID"},
                status_code=401,
            )
        else:
            reset_action = forgot_password_DB_inst.forgot_password_execute_query(req_body)
            if reset_action["reset"]:
                try:
                    logger.info(
                                "In function: send_mail_trigger_forgot_pass(email=%s, new_password=%s) returned: %s",       # pylint: disable=line-too-long
                                req_body["email"],
                                reset_action["new_password"],
                                forgot_password_DB_inst.send_mail_trigger_forgot_pass(req_body["email"], reset_action["new_password"]),       # pylint: disable=line-too-long
                            )

                    return JSONResponse(
                        content={"reset_link": True, "IT_alert": True}, status_code=202
                    )
                except Error as mail_error4:
                    logger.error("Failed to send mail: %s", mail_error4)
                    return JSONResponse(
                        content={
                            "reset_link": False,
                            "helpText": "failed to send mail",
                            "IT_alert": True,
                        },
                        status_code=500,
                    )
            else:
                return JSONResponse(
                    content={
                        "reset_link": False,
                        "helpText": "failed to generate password",
                        "IT_alert": True,
                    },
                    status_code=500,
                )
    else:
        return JSONResponse(
            content={"helpText": {"data": data}, "reset_link": False}, status_code=500
        )


@app.post("/data-api/change-password")
async def data_api_change_password(payload: Request):
    """Route function for change-password action"""

    req_body = await payload.json()
    change_password_DB_inst = DB_psycopg2()
    data = change_password_DB_inst.change_password_response_from_query(req_body)
    logger.info(data)
    # below 2 lines for testing
    # data[0] = ("qw",0)
    # data[0] = (12,0)
    if isinstance(data[0][0], int):
        if data[0][0] == 1:
            reset_action = change_password_DB_inst.change_password_execute_query(req_body)
            if reset_action["reset"]:                 # pylint: disable=no-else-return
                return JSONResponse(content={"reset": True}, status_code=201)
            else:
                return JSONResponse(
                    content={"reset": False, "helpText": "failed to reset password"},
                    status_code=500,
                )
        elif data[0][0] == 0:
            return JSONResponse(
                content={
                    "reset": False,
                    "uiText": "Please enter correct current password",
                },
                status_code=401,
            )
        else:
            reset_action = change_password_DB_inst.change_password_execute_query(req_body)
            if reset_action["reset"]:                 # pylint: disable=no-else-return
                return JSONResponse(
                    content={"reset": True, "IT_alert": True}, status_code=202
                )
            else:
                return JSONResponse(
                    content={
                        "reset": False,
                        "helpText": "failed to reset password",
                        "IT_alert": True,
                    },
                    status_code=500,
                )
    else:
        return JSONResponse(
            content={"helpText": {"data": data}, "reset": False}, status_code=500
        )


@app.get("/data-api/business-scenario/industry-dropdown")
async def data_api_business_scenario_industry_dropdown():
    """Route function for fetching data for the Industry dropdown in the Business Scenario tab"""

    business_scenario_industry_dropdown_inst = DB_psycopg2()
    data = business_scenario_industry_dropdown_inst.business_scenario_industry_dropdown()
    logger.info(data)
    return JSONResponse(content=data, status_code=200)

@app.post("/data-api/business-scenario/domain-dropdown")
async def data_api_business_scenario_domain_dropdown(payload: Request):
    """Route function for fetching data for the Domain dropdown in the Business Scenario tab"""

    req_body = await payload.json()
    business_scenario_domain_dropdown_inst = DB_psycopg2()
    data = business_scenario_domain_dropdown_inst.business_scenario_domain_dropdown(req_body)
    logger.info(data)
    return JSONResponse(content=data, status_code=200)


@app.post("/data-api/business-scenario/process-dropdown")
async def data_api_business_scenario_process_dropdown(payload: Request):
    """Route function for fetching data for the Process dropdown in the Business Scenario tab"""

    req_body = await payload.json()
    business_scenario_process_dropdown_inst = DB_psycopg2()
    data = business_scenario_process_dropdown_inst.business_scenario_process_dropdown(req_body)
    logger.info(data)
    return JSONResponse(content=data, status_code=200)


@app.get("/data-api/business-scenario/complete-dropdown")
async def data_api_business_scenario_complete_dropdown():
    """Route function for fetching data of all 3 dropdowns in the Business Scenario tab"""

    business_scenario_complete_dropdown_inst = DB_psycopg2()
    data_frame = pd.DataFrame(
        business_scenario_complete_dropdown_inst.business_scenario_complete_dropdown(),
        columns=["Business", "Domain", "Process"],
    )
    dct = {}
    for business in data_frame["Business"].unique():
        dct[business] = {}
    for business in data_frame["Business"].unique():
        data_frame1 = data_frame[data_frame["Business"] == business]
        for domain in data_frame1["Domain"].unique():
            dct[business][domain] = []
    for business in data_frame["Business"].unique():
        data_frame1 = data_frame[data_frame["Business"] == business]
        for domain in data_frame1["Domain"].unique():
            dct[business][domain] = list(
                data_frame[(data_frame["Business"] == business) & (data_frame["Domain"] == domain)]["Process"]  # pylint: disable=line-too-long
            )
    return JSONResponse(content=dct, status_code=200)


@app.post("/data-api/update-challenge-status")
async def update_challenge_status_api(payload: Request):
    """Route function for adding/updating entry of challenge_status table"""

    req_body = await payload.json()
    update_challenge_status_inst = DB_psycopg2()
    response, status_code = update_challenge_status_inst.update_challenge_status(req_body)
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/fetch-challenge-status")
async def fetch_challenge_status_api(payload: Request):
    """Route function for fetching an entry of challenge_status table"""

    req_body = await payload.json()
    fetch_challenge_status_inst = DB_psycopg2()
    response, status_code = fetch_challenge_status_inst.fetch_challenge_status(req_body)
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/challenge-json-data-write")
async def challenge_json_data_write(payload: Request):
    """Route function for adding/updating entry of/in challenge_json_data table"""

    req_body = await payload.json()
    challenge_json_data_write_inst = DB_psycopg2()
    response, status_code = challenge_json_data_write_inst.update_challenge_json(req_body)
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/challenge-json-data-fetch")
async def challenge_json_data_fetch(payload: Request):
    """Route function for fetching data for fetchting entry of challenge_status table"""

    req_body = await payload.json()
    challenge_json_data_fetch_inst = DB_psycopg2()
    response, status_code = challenge_json_data_fetch_inst.fetch_challenge_json(req_body)
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/challenge-creation")
async def challenge_creation_api(payload: Request):
    """Route function for challenge creation in challenge table"""

    req_body = await payload.json()
    challenge_creation_inst = DB_psycopg2()
    response, status_code = challenge_creation_inst.challenge_creation(req_body)
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/challenge-count")
async def challenge_count_api(payload: Request):
    """Route function for counting the number of challenges corresponding to a user_id"""

    req_body = await payload.json()
    challenge_count_inst = DB_psycopg2()
    response, status_code = challenge_count_inst.challenge_count(req_body)
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)