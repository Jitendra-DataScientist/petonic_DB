"""
    data-api routes
    primarily for connecting with the postgres database
"""
import os
import sys
import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import logging
import pandas as pd
import psycopg2
from psycopg2 import Error
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

# Create a logger instance
logger = logging.getLogger(__name__)


# CAUTION : the python script and .env file need to be in the same path for below line.
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
except Error as env_error:
    logger.critical("Failed to read DB params: %s", env_error)
    sys.exit()


# Create a FastAPI instance
app = FastAPI()


# Defining a route and a request handler function for health


@app.get("/data-api/health")
async def health():
    """Route funtion to return health status of data-api"""

    return JSONResponse(content={"API_status": "healthy"}, status_code=200)


# Defining a function for processing (a) query(queries) that return(s) some response(s)


def response_from_query(req_body, action):   # pylint: disable=too-many-branches
    """Function that executes (a) query (queries) and return(s) some data from the database"""

    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(**db_params)

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Query Formation
        if action == "login":
            query = "select count(*) \
                    from user_login as ul \
                    join validation as v \
                    on ul.user_id = v.user_id \
                    where ul.user_id = %s and ul.password = %s and v.user_id = %s;"
            query_data = (
                req_body["role"] + "_" + req_body["email"],
                req_body["password"],
                req_body["role"] + "_" + req_body["email"],
            )
        elif action == "forgot_password":
            query = "select count(*) \
                    from validation \
                    where user_id = %s;"
            query_data = (req_body["role"] + "_" + req_body["email"],)
        elif action == "change_password":
            query = "select count(*)\
                    from user_login as ul\
                    inner join validation as v\
                    on ul.user_id = v.user_id\
                    where ul.user_id = %s and ul.password = %s;"
            query_data = (
                req_body["role"] + "_" + req_body["email"],
                req_body["current_password"],
            )
        elif action == "business_scenario_industry_dropdown":
            query = "select *\
                    from industry_list;"
        elif action == "business_scenario_domain_dropdown":
            query = "select domain_id,name\
                    from domain_list\
                    where industry_id = %s;"
            query_data = (req_body["industry_id"],)
        elif action == "business_scenario_process_dropdown":
            query = "select process_id,name\
                    from process_list\
                    where domain_id = %s;"
            query_data = (req_body["domain_id"],)
        elif action == "business_scenario_complete_dropdown":
            query = "select il.name as industry, dl.name as domain, pl.name as process\
                    from industry_list as il\
                    join domain_list as dl\
                    on il.industry_id = dl.industry_id\
                    join process_list as pl\
                    on dl.domain_id = pl.domain_id;"

        # Execute the query
        if action in ("business_scenario_industry_dropdown", "business_scenario_complete_dropdown"):
            cursor.execute(query)
        else:
            cursor.execute(query, query_data)

        # Fetch data
        ret_data = cursor.fetchall()

        return ret_data

    except Exception as db_error:  # pylint: disable=broad-exception-caught
        exception_type, _, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno
        logger.error("%s||||%s||||%s", exception_type, filename, line_number)
        return {
            "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"
        }

    # except Error as e:
    #     logger.error(f"Error: {e}")

    finally:
        # Close the cursor and the database connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Defining a route and a request handler function for login


@app.post("/data-api/login")
async def data_api_login(payload: Request):
    """Route function for user login action"""

    req_body = await payload.json()
    data = response_from_query(req_body, action="login")
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


# Defining a function to generate a random password


def generate_random_string(str_len):
    """funtion to generate random set of characters
    for passwords, IDs etc."""
    # Define character sets
    digits = string.digits
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    # special_characters = string.punctuation

    # Combine character sets
    all_characters = (
        digits + lowercase_letters + uppercase_letters
    )  # + special_characters

    # Generate rand_str
    rand_str = "".join(random.choice(all_characters) for _ in range(str_len))

    return rand_str


# Defining a function for processing (a) query (queries) that do(does) not return any response(s)


def execute_query(req_body, action):         # pylint: disable=too-many-return-statements,too-many-branches,inconsistent-return-statements
    """function for processing (a) query (queries) that
    do(does) not return any response(s) from database"""
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(**db_params)

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Queries Formation
        if action == "signup":
            queries_list = [
                "INSERT INTO user_login (user_id, company_id, email, password, role) VALUES (%s, %s, %s, %s, %s);",  # pylint: disable=line-too-long
                "INSERT INTO user_signup (f_name, l_name, user_id) VALUES (%s, %s, %s);",
            ]

            query_data = [
                (
                    req_body["role"] + "_" + req_body["email"],
                    req_body["company_id"],
                    req_body["email"],
                    req_body["password"],
                    req_body["role"],
                ),
                (
                    req_body["f_name"],
                    req_body["l_name"],
                    req_body["role"] + "_" + req_body["email"],
                ),
            ]
        elif action == "validation":
            queries_list = ["INSERT INTO validation (user_id) VALUES (%s);"]

            query_data = [(req_body["role"] + "_" + req_body["email"],)]
        elif action in ("forgot_password", "change_password"):
            if action == "forgot_password":
                new_password = generate_random_string(str_len=8)
            elif action == "change_password":
                new_password = req_body["new_password"]
            queries_list = [
                "UPDATE user_login \
                            SET password = %s \
                            WHERE user_id = %s;"
            ]

            query_data = [(new_password, req_body["role"] + "_" + req_body["email"])]

        try:
            for query_count, query in enumerate(queries_list):
                # Execute the query
                cursor.execute(query, query_data[query_count])

                # Print a success message
                logger.info("Query %d executed successfully", query_count)

            # Commit the transaction
            connection.commit()

            if action == "signup":          # pylint: disable=no-else-return
                return {"user_creation": True}, 201
            elif action == "validation":
                return {"validation": True}, 200
            elif action == "forgot_password":
                return {"reset": True, "new_password": new_password}
            elif action == "change_password":
                return {"reset": True}

        except Exception as db_error:   # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            if action == "signup":          # pylint: disable=no-else-return
                return {
                    "user_creation": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",   # pylint: disable=line-too-long
                }, 400
            elif action == "validation":
                return {
                    "validation": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}",
                }, 400
            elif action == "forgot_password":
                return {
                    "reset": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}",
                }
            elif action == "change_password":
                return {
                    "reset": False,                  # pylint: disable=line-too-long
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}",
                }

    except Exception as db_error:           # pylint: disable=broad-exception-caught
        exception_type, _, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno
        logger.error("%s||||%s||||%d", exception_type, filename, line_number)
        if action == "signup":           # pylint: disable=no-else-return
            return {
                "user_creation": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",   # pylint: disable=line-too-long
            }, 500
        elif action == "validation":
            return {
                "validation": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}",
            }, 500
        elif action == "forgot_password":
            return {
                "reset": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}",
            }
        elif action == "change_password":
            return {
                "reset": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}",
            }
    # except Error as e:
    #     logger.error(f"Error: {e}")

    finally:
        # Close the cursor and the database connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Defining a route and a request handler function for signup


@app.post("/data-api/signup")
async def data_api_signup(payload: Request):
    """Route function for user signup action"""

    req_body = await payload.json()
    signup_response, status_code = execute_query(req_body, action="signup")
    return JSONResponse(content=signup_response, status_code=status_code)


# Defining a route and a request handler function for validation


@app.post("/data-api/validation")
async def data_api_validation(payload: Request):
    """Route function for user validation action"""

    req_body = await payload.json()
    validation_response, status_code = execute_query(req_body, action="validation")
    return JSONResponse(content=validation_response, status_code=status_code)


# Defining a function to send mail


def send_email(subject, body, to_email, sender_email, sender_password, smtp_server, image_path=None):      # pylint: disable=line-too-long,too-many-arguments
    """mail sender function"""
    # Set up the SMTP server
    smtp_port = 587

    # Create the email message
    msg = MIMEMultipart()
    msg["From"] = "Petonic Automail <" + sender_email + ">"
    msg["To"] = to_email
    msg["Subject"] = subject

    # Attach the email body as HTML
    msg.attach(MIMEText(body, "html"))

    # Attach the image if provided
    if image_path:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            image = MIMEImage(image_data, name=os.path.basename(image_path))
            # Set the Content-ID header
            image.add_header("Content-ID", "<company_logo>")
            msg.attach(image)

    # Set up the SMTP connection
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Start TLS for security
        server.starttls()

        # Login to the email server
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, to_email, msg.as_string())


# Defining a function to trigger send_mail
# Below function forms the mail body, gets the SMTP server
# details (loads from .env, if error then uses default).


def send_mail_trigger(to_email, new_password):
    """mail sender trigger function"""
    subject = "Password Reset"
    try:
        logo_url = os.getenv("logo_url")
        body = (
                f"""<p>Hello,<br>
                Your password has been reset to <strong>{new_password}</strong>.<br>
                Please log in using this password to reset your password.</p>
                <p>Best regards,<br>
                Petonic Team</p>
                <img src={logo_url} alt="Petonic Company Logo">"""
            )

    except Exception as mail_error:  # pylint: disable=broad-exception-caught
        logger.critical("Failed to load logo_url from .env: %s", mail_error)
        body = (
            """<p>Hello,<br>
        Your password has been reset to <strong>"""
            + new_password
            + """</strong>.<br>
        Please log in using this password to reset your password.</p>
        <p>Best regards,<br>
        Petonic Team</p>"""
        )

    # SMTP server details
    smtp_server = "smtp.gmail.com"
    try:
        sender_email = os.getenv("sender_email")
        sender_password = os.getenv("sender_password")
    except Exception as mail_error1:     # pylint: disable=broad-exception-caught
        logger.warning("Failed to fetch auto-mail creds from env: %s", mail_error1)
        sender_email = "automail.petonic@gmail.com"
        sender_password = "efvumbcfgryjachh"
        logger.critical("failed to load env, using default sender_email and sender_password")

    try:
        send_email(subject, body, to_email, sender_email, sender_password, smtp_server)
        logger.info("mail sent !!")
        return "mail sent !!"
    except Exception as mail_error2:   # pylint: disable=broad-exception-caught
        logger.critical("Mail sending error: %s", mail_error2)
        return "Mail sending error: ", mail_error2


# Defining a route and a request handler function for forgot-password button


@app.post("/data-api/forgot-password")
async def data_api_forgot_password(payload: Request):         # pylint: disable=too-many-return-statements
    """Route function for forgot-password action"""

    req_body = await payload.json()
    data = response_from_query(req_body, action="forgot_password")
    logger.info(data)
    # below 2 lines for testing
    # data[0] = ("qw",0)
    # data[0] = (12,0)
    if isinstance(data[0][0], int):
        if data[0][0] == 1:
            reset_action = execute_query(req_body, action="forgot_password")
            if reset_action["reset"]:
                try:
                    logger.info(                 # pylint: disable=logging-too-many-args
                        "In function: ",
                        send_mail_trigger(
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
            reset_action = execute_query(req_body, action="forgot_password")
            if reset_action["reset"]:
                try:
                    logger.info(
                                "In function: send_mail_trigger(email=%s, new_password=%s) returned: %s",       # pylint: disable=line-too-long
                                req_body["email"],
                                reset_action["new_password"],
                                send_mail_trigger(req_body["email"], reset_action["new_password"]),
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


# Defining a route and a request handler function for change password action


@app.post("/data-api/change-password")
async def data_api_change_password(payload: Request):
    """Route function for change-password action"""

    req_body = await payload.json()
    data = response_from_query(req_body, action="change_password")
    logger.info(data)
    # below 2 lines for testing
    # data[0] = ("qw",0)
    # data[0] = (12,0)
    if isinstance(data[0][0], int):
        if data[0][0] == 1:
            reset_action = execute_query(req_body, action="change_password")
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
            reset_action = execute_query(req_body, action="change_password")
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


# Defining a route and a request handler function for industry dropdown in "Business Scenario" tab


@app.get("/data-api/business-scenario/industry-dropdown")
async def data_api_business_scenario_industry_dropdown():
    """Route function for fetching data for the Industry dropdown in the Business Scenario tab"""

    data = response_from_query({}, action="business_scenario_industry_dropdown")
    logger.info(data)
    return JSONResponse(content=data, status_code=200)


# Defining a route and a request handler function for domain dropdown in "Business Scenario" tab


@app.post("/data-api/business-scenario/domain-dropdown")
async def data_api_business_scenario_domain_dropdown(payload: Request):
    """Route function for fetching data for the Domain dropdown in the Business Scenario tab"""

    req_body = await payload.json()
    data = response_from_query(req_body, action="business_scenario_domain_dropdown")
    logger.info(data)
    return JSONResponse(content=data, status_code=200)


# Defining a route and a request handler function for process dropdown in "Business Scenario" tab


@app.post("/data-api/business-scenario/process-dropdown")
async def data_api_business_scenario_process_dropdown(payload: Request):
    """Route function for fetching data for the Process dropdown in the Business Scenario tab"""

    req_body = await payload.json()
    data = response_from_query(req_body, action="business_scenario_process_dropdown")
    logger.info(data)
    return JSONResponse(content=data, status_code=200)


# Defining a route and a request handler function
# for data of all dropdowns under "Business Scenario" tab


@app.get("/data-api/business-scenario/complete-dropdown")
async def data_api_business_scenario_complete_dropdown():
    """Route function for fetching data of all 3 dropdowns in the Business Scenario tab"""

    data_frame = pd.DataFrame(
        response_from_query({}, action="business_scenario_complete_dropdown"),
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
