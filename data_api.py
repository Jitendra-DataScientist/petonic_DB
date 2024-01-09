"""
    this script hosts data-api routes
    that are written using FASTAPI
"""
import logging
from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
# from db_main import DBMain
from user_profile import UserProfile
from forgot_password import ForgotPassword
from change_password import ChangePassword
from business_scenario_dropdowns import BSD
from challenge_status import CS
from challenge_json import CJ
from challenge_generic import CG
import pydantic_check


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

# Create a logger instance
logger = logging.getLogger(__name__)


# db_main_inst = DBMain()
user_profile_inst = UserProfile()
forgot_pass_inst = ForgotPassword()
change_pass_inst = ChangePassword()
BSD_inst = BSD()
CS_inst = CS()
CJ_inst = CJ()
challenge_generic_inst = CG()


# Create a FastAPI instance
app = FastAPI()


@app.get("/data-api/health")
async def health():
    """Route funtion to return health status of data-api"""

    return JSONResponse(content={"API_status": "healthy"}, status_code=200)


@app.post("/data-api/login")
async def data_api_login(payload: pydantic_check.LoginRequest):
    """Route function for user login action"""

    # req_body = await payload.json()
    response, status_code = user_profile_inst.login_trigger(vars(payload))
    logger.info("Response: %s, Status Code: %s", response, status_code)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/signup")
async def data_api_signup(payload: pydantic_check.SignupRequest):
    """Route function for user signup action"""

    signup_response, status_code = user_profile_inst.signup(vars(payload))
    return JSONResponse(content=signup_response, status_code=status_code)


@app.post("/data-api/resend-mail-signup")
async def data_api_resend_signup_mail(payload: pydantic_check.ResendSignupMailRequest):
    """Route function for user signup action"""

    resend_response, status_code = user_profile_inst.resend_mail_signup(vars(payload))
    return JSONResponse(content=resend_response, status_code=status_code)


@app.post("/data-api/validation")
async def data_api_validation(payload: pydantic_check.ValidationRequest):
    """Route function for user validation action"""

    validation_response, status_code = user_profile_inst.validation(vars(payload))
    return JSONResponse(content=validation_response, status_code=status_code)


@app.post("/data-api/forgot-password")
async def data_api_forgot_password(payload: pydantic_check.ForgotPasswordRequest):
    """Route function for forgot-password action"""

    forgot_pass_response, status_code = forgot_pass_inst.forgot_password_main(payload.dict())
    return JSONResponse(content=forgot_pass_response, status_code=status_code)


@app.post("/data-api/change-password")
async def data_api_change_password(payload: pydantic_check.ChangePasswordRequest):
    """Route function for change-password action"""

    change_pass_response, status_code = change_pass_inst.change_password_main(vars(payload))
    return JSONResponse(content=change_pass_response, status_code=status_code)


@app.get("/data-api/business-scenario/industry-dropdown")
async def data_api_business_scenario_industry_dropdown():
    """Route function for fetching data for the
       Industry dropdown in the Business Scenario tab
    """

    data = BSD_inst.business_scenario_industry_dropdown()
    logger.info(data)
    return JSONResponse(content=data, status_code=200)


@app.post("/data-api/business-scenario/domain-dropdown")
async def data_api_business_scenario_domain_dropdown(payload: pydantic_check.DomainDropdownRequest):
    """Route function for fetching data for the
       Domain dropdown in the Business Scenario tab
    """

    data = BSD_inst.business_scenario_domain_dropdown(vars(payload))
    logger.info(data)
    return JSONResponse(content=data, status_code=200)


@app.post("/data-api/business-scenario/process-dropdown")
async def data_api_business_scenario_process_dropdown(payload: pydantic_check.ProcessDropdownRequest):             # pylint: disable=line-too-long
    """Route function for fetching data for the
       Process dropdown in the Business Scenario tab
    """

    data = BSD_inst.business_scenario_process_dropdown(vars(payload))
    logger.info(data)
    return JSONResponse(content=data, status_code=200)


@app.get("/data-api/business-scenario/complete-dropdown")
async def data_api_business_scenario_complete_dropdown():
    """Route function for fetching data of all
       3 dropdowns in the Business Scenario tab
    """

    data = BSD_inst.business_scenario_complete_dropdown()
    logger.info(data)
    return JSONResponse(content=data, status_code=200)


@app.post("/data-api/update-challenge-status")
async def update_challenge_status_api(payload: pydantic_check.UpdateChallengeStatusRequest):
    """Route function for adding/updating entry of challenge_status table"""

    response, status_code = CS_inst.update_challenge_status(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/fetch-challenge-status")
async def fetch_challenge_status_api(payload: pydantic_check.FetchChallengeStatusRequest):
    """Route function for fetching an entry of challenge_status table"""

    response, status_code = CS_inst.fetch_challenge_status(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/challenge-json-data-update")
async def challenge_json_data_update(payload: pydantic_check.ChallengeJsonDataWriteRequest):
    """Route function for adding/updating entry
       in/of challenge_json_data table
    """

    # req_body = await payload.json()
    response, status_code = CJ_inst.update_challenge_json(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/challenge-json-data-fetch")
async def challenge_json_data_fetch(payload: pydantic_check.ChallengeJsonDataFetchRequest):
    """Route function for fetching data for fetchting
       entry of challenge_status table
    """

    response, status_code = CJ_inst.fetch_challenge_json(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/challenge-initiation")
async def challenge_initiation_api(payload: pydantic_check.ChallengeInitiationRequest):
    """Route function for challenge creation in challenge table"""

    response, status_code = challenge_generic_inst.challenge_initiation(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/challenge-count")
async def challenge_count_api(payload: pydantic_check.ChallengeCountRequest):
    """Route function for counting the number
       of challenges corresponding to a user_id
    """

    response, status_code = challenge_generic_inst.challenge_count(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/challenge-creation")
async def challenge_creation_api(payload: pydantic_check.ChallengeCreationRequest):
    """Route function for updating challenge creation date in challenge table"""

    response, status_code = challenge_generic_inst.challenge_creation(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


# @app.route("/data-api/view-list", methods=["GET", "POST"])
# async def challenge_creation_api(request: Request = Depends(),
#                                  payload: pydantic_check.ViewListRequest = None):
#     """Route function for view-list page for all roles"""

#     if request.method == "GET":
#         response, status_code = challenge_generic_inst.view_list()
#     elif request.method == "POST":
#         if payload is None:
#             return JSONResponse(content={"error": "Payload is required for POST requests"},
#                                 status_code=400)
#         response, status_code = challenge_generic_inst.view_list(vars(payload))
#     logger.info(response)
#     return JSONResponse(content=response, status_code=status_code)


@app.route("/data-api/view-list", methods=["GET", "POST"])
async def view_list_api(request: Request = Depends()):
    """Route function for view-list page for all roles"""

    if request.method == "GET":
        response, status_code = challenge_generic_inst.view_list()
    elif request.method == "POST":
        try:
            payload = pydantic_check.ViewListRequest(**await request.json())
        except ValueError:
            return JSONResponse(content={"fetch": False,
                                         "data": None,
                                         "helpText":"Invalid JSON format in the request body"},
                                status_code=400)

        response, status_code = challenge_generic_inst.view_list(vars(payload))

    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)
