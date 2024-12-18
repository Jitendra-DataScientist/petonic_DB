"""
    this script hosts data-api routes
    that are written using FASTAPI
"""
import os
import logging
from typing import List, Dict
from fastapi import FastAPI, Request, Depends, File, UploadFile, Form, Body, BackgroundTasks
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
# from db_main import DBMain
from user_profile import UserProfile
from forgot_password import ForgotPassword
from change_password import ChangePassword
from business_scenario_dropdowns import business_scenario_complete_dropdown
from challenge_status import CS
from challenge_json import CJ
from contributor_approver_json import CAJ
from contributor_approver_generic import CAG
from challenge_generic import CG
from setting_parameter_tab import setting_parameter_key_parameters
from file_transfer import FT
import pydantic_check
from admin import Admin
from project_management import PM
from subscription import Subscription
from leaderboard import Leaderboard
from support import Support
from demo import Demo
from sensitive import Sensitive


# Determine the directory for logs
log_directory = os.path.join(os.getcwd(), 'logs')

# Create the logs directory if it doesn't exist
if not os.path.exists(log_directory):
    os.mkdir(log_directory)

# Configure logging
# logging.basicConfig(
#     filename="logs.log"
#     level=logging.DEBUG,
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     handlers=[logging.StreamHandler()],
# )

# Create a logger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler for this script's log file
file_handler = logging.FileHandler(os.path.join(log_directory, "data_api.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


# db_main_inst = DBMain()
user_profile_inst = UserProfile()
forgot_pass_inst = ForgotPassword()
change_pass_inst = ChangePassword()
# BSD_inst = BSD()
CS_inst = CS()
CJ_inst = CJ()
contributor_approver_json_inst = CAJ()
contributor_approver_generic_inst = CAG()
challenge_generic_inst = CG()
user_details_instance = Admin()
file_transfer_instance = FT()
project_management_instance = PM()
subscription_instance = Subscription()
leaderboard_instance = Leaderboard()
support_instance = Support()
demo_instance = Demo()
sensitive_inst = Sensitive()


# Create a FastAPI instance
app = FastAPI()

# Allowing all origins for now
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


# @app.get("/data-api/business-scenario/industry-dropdown")
# async def data_api_business_scenario_industry_dropdown():
#     """Route function for fetching data for the
#        Industry dropdown in the Business Scenario tab
#     """

#     data = BSD_inst.business_scenario_industry_dropdown()
#     logger.info(data)
#     if data:             # pylint: disable=no-else-return)
#         return JSONResponse(content=data, status_code=200)
#     else:
#         return JSONResponse(content=data, status_code=500)


# @app.post("/data-api/business-scenario/domain-dropdown")
# async def data_api_business_scenario_domain_dropdown(
#     payload: pydantic_check.DomainDropdownRequest
#     ):
#     """Route function for fetching data for the
#        Domain dropdown in the Business Scenario tab
#     """

#     data = BSD_inst.business_scenario_domain_dropdown(vars(payload))
#     logger.info(data)
#     if data:             # pylint: disable=no-else-return)
#         return JSONResponse(content=data, status_code=200)
#     else:
#         return JSONResponse(content=data, status_code=400)


# @app.post("/data-api/business-scenario/process-dropdown")
# async def data_api_business_scenario_process_dropdown(
#     payload: pydantic_check.ProcessDropdownRequest
#     ):
#     """Route function for fetching data for the
#        Process dropdown in the Business Scenario tab
#     """

#     data = BSD_inst.business_scenario_process_dropdown(vars(payload))
#     logger.info(data)
#     if data:             # pylint: disable=no-else-return)
#         return JSONResponse(content=data, status_code=200)
#     else:
#         return JSONResponse(content=data, status_code=400)


@app.get("/data-api/business-scenario/complete-dropdown")
async def data_api_business_scenario_complete_dropdown():
    """Route function for fetching data of all
       3 dropdowns in the Business Scenario tab
    """

    data = business_scenario_complete_dropdown()
    # logger.info(data)
    if data:             # pylint: disable=no-else-return)
        return JSONResponse(content=data, status_code=200)
    else:
        return JSONResponse(content=data, status_code=500)


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


# @app.route("/data-api/view-list", methods=["GET", "POST"])
# async def view_list_api(request: Request = Depends()):
#     """Route function for view-list page for all roles"""

#     if request.method == "GET":
#         response, status_code = challenge_generic_inst.view_list()
#     elif request.method == "POST":
#         try:
#             payload = pydantic_check.ViewListRequest(**await request.json())
#         except ValueError:
#             return JSONResponse(content={"fetch": False,
#                                          "data": None,
#                                          "helpText":"Invalid format in the request body"},
#                                 status_code=400)

#         response, status_code = challenge_generic_inst.view_list(vars(payload))

#     logger.info(response)
#     return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/view-list")
async def view_list_api(payload: pydantic_check.ViewListRequest):
    """Route function for view-list page for all roles"""

    response, status_code = challenge_generic_inst.view_list(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/flip-user-status")
async def flip_user_status_api(payload: pydantic_check.FlipUserStatusRequest):
    """Route function for deactivating a user account from User Management page"""

    response, status_code = user_details_instance.flip_user_status(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/edit-user-details")
async def edit_user_api(payload: pydantic_check.EditUserDetailsRequest):
    """Route function for editing user details"""

    response, status_code = user_details_instance.edit_details(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/admin-view-list")
async def admin_view_list_api(payload: pydantic_check.AdminViewListRequest):
    """Route function to fetch data for admin list view"""

    response, status_code = user_details_instance.admin_view_list(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/setting-parameter-key-parameters")
async def setting_parameter_key_factors_api(
    payload: pydantic_check.SettinParamaterKeyParametersRequest
    ):
    """Route function to fetch data for "Setting
       Parameters" tab's key parameters"""

    data = setting_parameter_key_parameters(vars(payload))
    logger.info(data)
    if data:             # pylint: disable=no-else-return)
        return JSONResponse(content=data, status_code=200)
    else:
        return JSONResponse(content=data, status_code=400)


@app.post("/data-api/contributor-approver-json-data-update")
async def contributor_approver_json_data_update(
    payload: pydantic_check.ContributorApproverJsonDataWriteRequest
    ):
    """Route function for adding/updating json
       entry in/of contributor_approver table
    """

    # req_body = await payload.json()
    response, status_code = contributor_approver_json_inst.update_json(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/contributor-approver-json-data-fetch")
async def contributor_approver_json_data_fetch(
    payload: pydantic_check.ContributorApproverJsonDataFetchRequest
    ):
    """Route function for fetching data for fetchting
       json entry of contributor_approver table
    """

    response, status_code = contributor_approver_json_inst.fetch_json(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


# @app.post("/data-api/add-contributor")
# async def add_contributor(payload: pydantic_check.AddContributorRequest):
#     """Route function for adding a contributor_id
#        to contributor_approver table for a specific
#        challenge.
#     """

#     response, status_code = contributor_approver_generic_inst.add_contributor(vars(payload))
#     logger.info(response)
#     return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/add-approver")
async def add_approver(payload: pydantic_check.AddApproverRequest):
    """Route function for adding a approver_id
       to contributor_approver table for a specific
       challenge.
    """

    response, status_code = contributor_approver_generic_inst.add_approver(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)

### bookmark
@app.post("/data-api/add-approver-comment")
async def add_approver_comment(payload: pydantic_check.AddApproverCommentRequest):
    """Route function for adding approver's comment
       to contributor_approver table for a specific
       challenge.
    """

    response, status_code = contributor_approver_generic_inst.add_approver_comment(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/file-upload")
async def file_upload(path_key: str = Form(...), files: List[UploadFile] = File(...)):
    """Route function for uploading file(s)
    """

    response, status_code = file_transfer_instance.file_upload(path_key, files)
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/file-download")
async def file_download(payload: Dict[str, str] = Body(...)):
    """Route function for downloading a file
    """

    response, status_code = file_transfer_instance.file_download(payload)
    logger.info(response)
    try:
        return JSONResponse(content=response, status_code=status_code)
    except TypeError:
        return response


@app.post("/data-api/view-file-list")
async def view_file_list(payload: pydantic_check.ViewFileListRequest):
    """Route function for downloading a file
    """

    response, status_code = file_transfer_instance.view_file_list(vars(payload))
    logger.info(response)
    try:
        return JSONResponse(content=response, status_code=status_code)
    except TypeError:
        return response


@app.post("/data-api/contributor-solution-upload")
async def contributor_solution_upload_api(payload: pydantic_check.ContributorSolutionUploadRequest):
    """Route function for downloading a file
    """

    response, status_code = contributor_approver_json_inst.contributor_solution_upload(
                                                                         vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/get-user-details")
async def get_user_details_api(payload: pydantic_check.GetUserDetailsRequest):
    """Route function to fetch user details based on email IDs"""

    response, status_code = user_profile_inst.get_user_details(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/project-initiate")
async def project_initiate_api(payload: pydantic_check.ProjectInitiateRequest):
    """Route function to add project manager name
       and project management tool eing used, to DB
    """

    response, status_code = project_management_instance.project_initiation(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/first-add")
async def first_add(payload: pydantic_check.FirstAdd):
    """Route function to add first basic details of subscriber
    """

    response, status_code = subscription_instance.firstAdd(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/verify-otp")
async def verify_otp(payload: pydantic_check.VerifyOTP):
    """Route function to verify OTP of subsciber
    """

    response, status_code = subscription_instance.verifyOTP(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/resend-otp")
async def resend_otp(payload: pydantic_check.ResendOTP):
    """Route function to resend OTP of subsciber
    """

    response, status_code = subscription_instance.resendOTP(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/email-modify")
async def email_modify(payload: pydantic_check.EmailModify):
    """Route function to update (change) email address.
    """

    response, status_code = subscription_instance.emailModify(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/second-add")
async def second_add(payload: pydantic_check.SecondAdd):
    """Route function to add payment details of subscriber
    """

    response, status_code = subscription_instance.secondAdd(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/first-user")
async def firstUser(payload: pydantic_check.FirstUser):
    """Route function to check if a user is a first time user
    """

    response, status_code = user_profile_inst.checkFirstUser(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/flip-first-user-status")
async def flipFirstUserStatus(payload: pydantic_check.FlipFirstUserStatus):
    """Route function to flip first-time-user-status
       after first-time user changes password
    """

    response, status_code = user_profile_inst.flipFirstUserStatus(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/leaderboard/best-project")
async def leaderboard_best_project(payload: pydantic_check.LeaderboardBestProject):
    """Route function to return the details of approved
       challenges for projects (for leaderboard page)
    """

    response, status_code = leaderboard_instance.best_project(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/solvai-support")
async def solvai_support(payload: pydantic_check.SolvaiSupport):
    """Route function for SolvAI support feature.
    """

    response, status_code = support_instance.solvai_support(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/petonicai-support")
async def petonicai_support(payload: pydantic_check.PetonicaiSupport):
    """Route function for "Contact Us" page of petonic.ai website.
    """

    response, status_code = support_instance.petonicai_support(vars(payload), "petonicai_support")
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/solvai-demo")
async def solvai_demo(payload: pydantic_check.SolvaiDemo):
    """Route function for Request-Demo support feature of SolvAI.
    """

    response, status_code = demo_instance.solvai_demo(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


def delete_file(file_path: str):
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Error deleting file: {e}")

@app.post("/data-api/csv-file-download/")
async def generate_csv(background_tasks: BackgroundTasks, payload: dict = Body(...)):

    # Creating a pandas DataFrame
    df = pd.DataFrame(payload["data"], columns=payload["column_names"])

    # Saving the DataFrame to a CSV file
    df.to_csv(payload["filename"], index=False)

    # Add the file deletion to background tasks to run after the response is sent
    background_tasks.add_task(delete_file, payload["filename"])

    # Return the CSV file as a downloadable file
    return FileResponse(payload["filename"], media_type="text/csv", filename=payload["filename"])


@app.post("/data-api/plannex-support")
async def plannex_support(payload: pydantic_check.PetonicaiSupport):
    """Route function for Plannex website's "Book An Appointment" page.
    """

    response, status_code = support_instance.petonicai_support(vars(payload), "plannex_support")
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.get("/data-api/sensitive/tables")
async def tables():
    """Route fetching table names"""
    response, status_code = sensitive_inst.tables()
    return JSONResponse(content=response, status_code=status_code)


@app.get("/data-api/sensitive/table-data/{table_name}")
async def table_data(table_name: str):
    """Route fetching table data"""
    response, status_code = sensitive_inst.table_data(table_name)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/plannex-contact-us")
async def plannex_contact_us(payload: pydantic_check.PlannexContactUs):
    """Route function for Plannex website's "Contact Us" page.
    """

    response, status_code = support_instance.plannex_contact_us(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/data-api/plannex-login")
async def plannex_login(payload: pydantic_check.PlannexLogin):
    """Route function for Plannex website's login page.
    """

    response, status_code = user_profile_inst.plannex_login(vars(payload))
    logger.info(response)
    return JSONResponse(content=response, status_code=status_code)
