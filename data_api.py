"""
    this script hosts data-api routes
    that are written on FASTAPI
"""
import logging
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from DB_main import DB_main
from utils import utils


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

# Create a logger instance
logger = logging.getLogger(__name__)


db_main_inst = DB_main()


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
    data = db_main_inst.login(req_body)
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
    signup_response, status_code = db_main_inst.signup(req_body)
    return JSONResponse(content=signup_response, status_code=status_code)


@app.post("/data-api/validation")
async def data_api_validation(payload: Request):
    """Route function for user validation action"""

    req_body = await payload.json()
    validation_response, status_code = db_main_inst.validation(req_body)
    return JSONResponse(content=validation_response, status_code=status_code)


@app.post("/data-api/forgot-password")
async def data_api_forgot_password(payload: Request):         # pylint: disable=too-many-return-statements
    """Route function for forgot-password action"""

    req_body = await payload.json()
    forgot_pass_response, status_code = db_main_inst.forgot_password_main(req_body)
    return JSONResponse(content=forgot_pass_response, status_code=status_code)


@app.post("/data-api/change-password")
async def data_api_change_password(payload: Request):
    """Route function for change-password action"""

    req_body = await payload.json()
    change_pass_response, status_code = db_main_inst.change_password_main(req_body)
    return JSONResponse(content=change_pass_response, status_code=status_code)


@app.get("/data-api/business-scenario/industry-dropdown")
async def data_api_business_scenario_industry_dropdown():
    """Route function for fetching data for the Industry dropdown in the Business Scenario tab"""

    data = db_main_inst.business_scenario_industry_dropdown()
    logger.info(data)
    return JSONResponse(content=data, status_code=200)


@app.post("/data-api/business-scenario/domain-dropdown")
async def data_api_business_scenario_domain_dropdown(payload: Request):
    """Route function for fetching data for the Domain dropdown in the Business Scenario tab"""

    req_body = await payload.json()
    data = db_main_inst.business_scenario_domain_dropdown(req_body)
    logger.info(data)
    return JSONResponse(content=data, status_code=200)


@app.post("/data-api/business-scenario/process-dropdown")
async def data_api_business_scenario_process_dropdown(payload: Request):
    """Route function for fetching data for the Process dropdown in the Business Scenario tab"""

    req_body = await payload.json()
    data = db_main_inst.business_scenario_process_dropdown(req_body)
    logger.info(data)
    return JSONResponse(content=data, status_code=200)


@app.get("/data-api/business-scenario/complete-dropdown")
async def data_api_business_scenario_complete_dropdown():
    """Route function for fetching data of all 3 dropdowns in the Business Scenario tab"""

    data_frame = pd.DataFrame(
        db_main_inst.business_scenario_complete_dropdown(),
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
    response, status_code = db_main_inst.update_challenge_status(req_body)
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/fetch-challenge-status")
async def fetch_challenge_status_api(payload: Request):
    """Route function for fetching an entry of challenge_status table"""

    req_body = await payload.json()
    response, status_code = db_main_inst.fetch_challenge_status(req_body)
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/challenge-json-data-write")
async def challenge_json_data_write(payload: Request):
    """Route function for adding/updating entry of/in challenge_json_data table"""

    req_body = await payload.json()
    response, status_code = db_main_inst.update_challenge_json(req_body)
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/challenge-json-data-fetch")
async def challenge_json_data_fetch(payload: Request):
    """Route function for fetching data for fetchting entry of challenge_status table"""

    req_body = await payload.json()
    response, status_code = db_main_inst.fetch_challenge_json(req_body)
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/challenge-creation")
async def challenge_creation_api(payload: Request):
    """Route function for challenge creation in challenge table"""

    req_body = await payload.json()
    response, status_code = db_main_inst.challenge_creation(req_body)
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/challenge-count")
async def challenge_count_api(payload: Request):
    """Route function for counting the number of challenges corresponding to a user_id"""

    req_body = await payload.json()
    response, status_code = db_main_inst.challenge_count(req_body)
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)