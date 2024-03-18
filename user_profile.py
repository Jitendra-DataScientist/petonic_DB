"""
    this code primarily contains the user profile funtions for
    connecting to python code to PostgreSQL database by calling
    relevant pyscopg2 operation files (CRUD)
"""
import os
import sys
import logging
import json
import time
from db_return import db_return
from db_no_return import db_no_return
from utils import Utils


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
file_handler = logging.FileHandler(os.path.join(log_directory, "user_profile.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


utils = Utils()


class UserProfile:
    """
       this class primarily contains the user profile funtions
       to connect python code to PostgreSQL database by
       calling relevant pyscopg2 operation files (CRUD)
    """

    def __init__(self):
        self.user_profile_file = "logs/user_profile.json"
        # Check if user_profile.json exists, if not, create it
        if not os.path.exists(self.user_profile_file):
            with open(self.user_profile_file, "w", encoding="utf-8") as file_handle:
                file_handle.write("{}")  # Write empty JSON object


    def login(self, req_body):
        """Function for the login functionality.
           Check the count of rows after join.
        """

        try:
            query = "select count(*) \
                    from user_login as ul \
                    join validation as v \
                    on ul.email = v.email \
                    where ul.email = %s and ul.password = %s and v.active = 'true';"
            query_data = (
                req_body["email"],
                req_body["password"],
            )

            # Fetch data
            ret_data = db_return(query, query_data)
            role = None
            if isinstance(ret_data[0][0], int):
                if ret_data[0][0] >= 1:
                    query = "select role, f_name, l_name, employee_id\
                            from user_signup\
                            where user_signup.email = %s;"
                    query_data = (
                        req_body["email"],
                    )
                    role = db_return(query, query_data)
                else:
                    role = [("incorrect creds / inactive account / email not validated",
                             "incorrect creds / inactive account / email not validated",
                             "incorrect creds / inactive account / email not validated",
                             "incorrect creds / inactive account / email not validated",)]
            try:
                ret_data.append(role[0][0])
                ret_data.append(role[0][1])
                ret_data.append(role[0][2])
                ret_data.append(role[0][3])
            except KeyError:
                ret_data.append(None)
                ret_data.append(None)
                ret_data.append(None)
                ret_data.append(None)
            return ret_data

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
            }


    def login_trigger(self, req_Body):
        """Function to trigger above login
           funtion, and return response
        """

        try:
            req_body = req_Body.copy()
            req_body['email'] = req_body['email'].lower()
            data = self.login(req_body)
            logger.info(data)
            # below 2 lines for testing
            # data[0] = ("qw",0)
            # data[0] = (12,0)
            if isinstance(data[0][0], int):
                if data[0][0] == 1:                  # pylint: disable=no-else-return
                    return {"login": True,
                            "role": data[1],
                            "f_name": data[2],
                            "l_name": data[3],
                            "employee_id": data[4]}, 200
                elif data[0][0] == 0:
                    return {"login": False,
                            "helpText": data[1]}, 401
                else:
                    return {"login": True,
                            "IT_alert": True,
                            "role": data[1],
                            "f_name": data[2],
                            "l_name": data[3],
                            "employee_id": data[4]}, 202
            else:
                return {"helpText": {"data": data}, "login": False}, 401

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s||||%s", exception_type, filename, line_number, db_error)
            return {"login": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
                    }, 500


    def signup(self, req_Body):  # pylint: disable=too-many-locals,too-many-return-statements
        """function for signup funtionality"""
        try:
            req_body = req_Body.copy()
            req_body['email'] = req_body['email'].lower()
            req_body['admin_email'] = req_body['admin_email'].lower()
            # check if admin role
            query = "select role \
                    from user_signup\
                    where email = %s;"
            query_data = (
                req_body["email"],
            )

            role_data = db_return(query, query_data)

            if role_data and role_data[0] and role_data[0][0]=='admin'\
                    and req_body["role"] == "admin":  # pylint: disable=no-else-return
                return {"user_creation": False,
                        "helpText": "admin role already created"}, 400
            elif role_data and role_data[0] and role_data[0][0]=='admin':
                return {"user_creation": False,
                        "helpText": "Primary-key Violation Error"}, 400

            # verify admin creds for roles other than admin
            if req_body["role"] != "admin":
                try:
                    if self.login(
                        {"email":req_body["admin_email"],
                        "password":req_body["admin_password"]
                        }
                        )[1] == "admin":
                        pass
                    else:
                        return {"user_creation": False,
                                "helpText": "invalid admin creds"}, 400
                except Exception as admin_auth:  # pylint: disable=broad-exception-caught
                    logger.info("admin_auth: %s", admin_auth)
                    return {"user_creation": False,
                            "helpText": "admin authorisation error"}, 500

            # Queries Formation
            first_password = utils.generate_random_string(str_len=8)

            queries_list = [
                "INSERT INTO user_login (email, password)\
                VALUES (%s, %s);",
                "INSERT INTO user_signup\
                (f_name, l_name, email, role, employee_id)\
                VALUES (%s, %s, %s, %s, %s);",
            ]

            query_data = [
                (
                    req_body["email"],
                    first_password,
                ),
                (
                    req_body["f_name"],
                    req_body["l_name"],
                    req_body["email"],
                    req_body["role"],
                    req_body["employee_id"],
                ),
            ]

            try:
                res = db_no_return(queries_list, query_data)

                if res == "success":
                    # Read existing user profile data
                    with open(self.user_profile_file, "r", encoding="utf-8") as file_handle:
                        user_profile_data = json.load(file_handle)

                    # Update user profile data with new user information
                    user_profile_data[req_body["email"]] = {req_body["role"]: [time.time()]}


                    # Write updated user profile data back to the file
                    with open(self.user_profile_file, "w", encoding="utf-8") as file_handle:
                        json.dump(user_profile_data, file_handle)

                    if utils.send_mail_trigger_signup(req_body["email"],                  # pylint: disable=no-else-return
                                                      first_password, req_body["role"]):
                        return {"user_creation": True}, 201
                    else:
                        return {"user_creation": False,
                                "helpText": "Failed to send email"}, 500
                else:
                    res.update({"user_creation": False})
                    return res, 400

            except Exception as db_error:  # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%s", exception_type, filename, line_number, db_error)      # pylint: disable=line-too-long
                return {
                    "user_creation": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                }, 400

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%s", exception_type, filename, line_number, db_error)
            return {
                "user_creation": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500


    def resend_mail_signup(self, req_Body):  # pylint: disable=too-many-return-statements
        """funtionality to resend signup mail with a
           different password, rest creds remain the same"""
        try:
            req_body = req_Body.copy()
            req_body['email'] = req_body['email'].lower()
            req_body['admin_email'] = req_body['admin_email'].lower()
            # verify admin creds
            try:
                if self.login(
                    {"email":req_body["admin_email"],
                    "password":req_body["admin_password"]
                    }
                    )[1] == "admin":
                    pass
                else:
                    return {"resend": False,
                            "helpText": "invalid admin creds"}, 400
            except Exception as admin_auth:  # pylint: disable=broad-exception-caught
                logger.info("admin_auth: %s", admin_auth)
                return {"resend": False,
                        "helpText": "admin authorisation error"}, 500

            new_password = utils.generate_random_string(str_len=8)
            queries_list = [
                "UPDATE user_login \
                SET password = %s \
                WHERE email = %s;"
            ]

            query_data = [(new_password, req_body["email"])]

            try:
                res = db_no_return(queries_list, query_data)

                if res == "success":   # pylint: disable=no-else-return
                    if utils.send_mail_trigger_signup(req_body["email"],                  # pylint: disable=no-else-return
                                                      new_password, req_body["role"]):
                        return {"resend": True}, 201
                    else:
                        return {"resend": False,
                                "helpText": "Failed to send email"}, 500
                else:
                    res.update({"resend": False})
                    return res, 400

            except Exception as db_error:  # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d", exception_type, filename, line_number)
                return {
                        "resend": False,
                        "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                    }, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                    "resend": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                }, 500


    def validation(self, req_Body):
        """function for email-validation funtionality
           after user signup
        """
        try:
            req_body = req_Body.copy()
            req_body['email'] = req_body['email'].lower()
            # Queries Formation
            queries_list = ["INSERT INTO validation (email, active) VALUES (%s, %s);"]

            query_data = [(req_body["email"], True)]

            try:
                res = db_no_return(queries_list, query_data)

                if  res == "success":   # pylint: disable=no-else-return
                    return {"validation": True}, 201
                else:
                    res.update({"validation": False})
                    return res, 400

            except Exception as db_error:  # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d", exception_type, filename, line_number)
                return {
                    "validation": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                }, 400

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                "validation": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500


    def get_user_details(self, req_body):
        """
            function to fetch details of users
            based on email IDs.
        """
        try:
            if not req_body["user_ids"]:
                return {"fetch": False,
                        "helpText": "no user_id passed",}, 400
            # Queries Formation
            query = "SELECT us.email,us.role,us.employee_id,us.f_name,us.l_name,v.active\
                    FROM user_signup us\
                    LEFT JOIN validation v ON us.email = v.email\
                    WHERE us.email IN %s;"
            query_data = (
                        tuple(req_body["user_ids"]),
                    )
            ret_data = db_return(query, query_data)
            if ret_data:
                mod_ret_data = {element[0]: element[1:] for element in ret_data}
            else:
                mod_ret_data = {}
            return {"fetch": True,
                    "data": mod_ret_data,
                    "fields":["role", "employee_id", "f_name", "l_name", "active"]}, 200

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                "fetch": False,
                "fields":["role", "employee_id", "f_name", "l_name", "active"],
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500
