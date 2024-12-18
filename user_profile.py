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
import requests
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
                    query = "select us.role, us.f_name, us.l_name, us.employee_id, ul.subscription_id\
                            from user_signup us\
                            join user_login ul\
                            on us.email=ul.email\
                            where us.email = %s;"
                    query_data = (
                        req_body["email"],
                    )
                    role = db_return(query, query_data)
                else:
                    role = [("incorrect creds / inactive account / email not validated",
                             "incorrect creds / inactive account / email not validated",
                             "incorrect creds / inactive account / email not validated",
                             "incorrect creds / inactive account / email not validated",
                             "incorrect creds / inactive account / email not validated",)]
            try:
                ret_data.append(role[0][0])
                ret_data.append(role[0][1])
                ret_data.append(role[0][2])
                ret_data.append(role[0][3])
                ret_data.append(role[0][4])
            except KeyError:
                ret_data.append(None)
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


    def fetch_online_status(self, sub_id, chat_ip, chat_port, fetch_online_status_payload):

        url = f"http://{str(chat_ip)}:{str(chat_port)}/fetch-online-users"
        payload = {
            "subscription_id": sub_id,
            "user_ids": "all"
        }
        res = requests.post(url=url,json=fetch_online_status_payload).json()
        return res


    def login_trigger(self, request_body):
        """Function to trigger above login
           funtion, and return response
        """

        try:
            req_body = request_body.copy()
            req_body['email'] = req_body['email'].lower()
            data = self.login(req_body)
            logger.info(data)
            # below 2 lines for testing
            # data[0] = ("qw",0)
            # data[0] = (12,0)
            if isinstance(data[0][0], int):
                if len(data) > 5:
                    sub_id = data[5]
                    chat_ip = os.getenv("chat_ip", "125.63.120.194")
                    chat_port = os.getenv("chat_port", 8011)
                    fetch_online_status_payload = {
                                                "subscription_id": data[5],
                                                "user_ids": "all"
                                            }
                    online_status = self.fetch_online_status(sub_id, chat_ip, chat_port, fetch_online_status_payload)
                    if isinstance(online_status, dict):
                        if "fetch" not in online_status:
                            return {"login": False,
                                    "helpText":"failed to retrieve proper response from fetch-online-users API"}, 500
                        else:
                            if not online_status["fetch"]:
                                if online_status["helpText"] == "unknown subscription_id" and data[5] == "incorrect creds / inactive account / email not validated":
                                    return {"login": False,
                                            "helpText": "incorrect creds / inactive account / email not validated"}, 400
                                else:
                                    return {"login": False, "online_status": online_status, "subscription_id": data[5],
                                            "helpText": "failed to retrieve proper response from fetch-online-users API with fetch as False"}, 500
                            else:
                                if req_body['email'] in online_status["data"]:
                                    if online_status["data"][req_body['email']]['status']:
                                        return {"login": False,
                                                "helpText":"user already logged in"}, 400
                    else:
                        return {"login": False,
                                "helpText":"failed to load online statuses"}, 500

                    if data[0][0] == 1:                  # pylint: disable=no-else-return
                        return {"login": True,
                                "role": data[1],
                                "f_name": data[2],
                                "l_name": data[3],
                                "employee_id": data[4],
                                "subscription_id": data[5]}, 200
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
                    return {"helpText": "unable to identify associated subscription_id",
                            "login": False,
                            "data": data}, 400

            else:
                return {"helpText":
                           {"data":data},
                        "login": False}, 401

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s||||%s", exception_type, filename, line_number, db_error)
            return {"login": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
                    }, 500


    def signup(self, request_body):  # pylint: disable=too-many-locals,too-many-return-statements
        """function for signup funtionality"""
        try:
            req_body = request_body.copy()
            req_body['email'] = req_body['email'].lower()
            try:
                req_body['admin_email'] = req_body['admin_email'].lower()
            except AttributeError:
                pass
            except KeyError:
                pass
            # check if admin role
            query = "select role \
                    from user_signup\
                    where email = %s;"
            query_data = (
                req_body["email"],
            )

            role_data = db_return(query, query_data)

            # if req_body['role'] == 'admin':
            query = "select count(*) from subscription where subscription_id = %s;"
            query_data = (
                req_body["subscription_id"],
            )
            subscription_data = db_return(query, query_data)
            if subscription_data and subscription_data[0] and subscription_data[0][0]==1:
                pass
            else:
                return {"user_creation": False,
                        "helpText": "mail not in subscription"}, 400


            if role_data and role_data[0] and role_data[0][0]=='admin'\
                    and req_body["role"] == "admin":  # pylint: disable=no-else-return
                return {"user_creation": False,
                        "helpText": "admin role already created for this email"}, 400
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

            # verify if the subscription plan permits addition of more users
            if req_body["role"] != "admin":
                try:
                    query = "select users_count from subscription where subscription_id = %s;"
                    query_data = (
                        req_body["subscription_id"],
                    )
                    user_count_allowed = db_return(query, query_data)
                    query = """SELECT count(*)
                            FROM user_login ul
                            LEFT JOIN user_signup us
                            ON ul.email = us.email
                            WHERE ul.subscription_id = %s
                            AND us.role <> 'admin';"""
                    query_data = (
                        req_body["subscription_id"],
                    )
                    user_count_actual = db_return(query, query_data)
                    if user_count_actual >= user_count_allowed:
                        return {"user_creation": False,
                                "helpText": "subscription user count limit reached"}, 401
                except Exception as count_error:
                    return {"user_creation": False,
                            "helpText": count_error}, 500


            # Queries Formation
            first_password = utils.generate_random_string(str_len=8)

            queries_list = [
                "INSERT INTO user_login (email, password, subscription_id, first_time)\
                VALUES (%s, %s, %s, %s);",
                "INSERT INTO user_signup\
                (f_name, l_name, email, role, employee_id)\
                VALUES (%s, %s, %s, %s, %s);",
            ]

            query_data = [
                (
                    req_body["email"],
                    first_password,
                    req_body["subscription_id"],
                    True
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


    def resend_mail_signup(self, request_body):  # pylint: disable=too-many-return-statements
        """funtionality to resend signup mail with a
           different password, rest creds remain the same"""
        try:
            req_body = request_body.copy()
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


    def validation(self, request_body):
        """function for email-validation funtionality
           after user signup
        """
        try:
            req_body = request_body.copy()
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


    def get_user_details(self, request_body):
        """
            function to fetch details of users
            based on email IDs.
        """
        try:
            if not request_body["user_ids"]:    # pylint: disable=no-else-return
                return {"fetch": False,
                        "helpText": "no user_id passed",}, 400
            else:
                req_body = request_body.copy()
                req_body["user_ids"] = [item.lower() for item in req_body['user_ids']]
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


    def checkFirstUser(self, req_body):
        """function to check if a user is a first time user
        """
        try:
            query = "select first_time from user_login where email = %s;"
            query_data = (
                req_body["email"],
            )
            first_user_data = db_return(query, query_data)
            if not first_user_data:
                return {"first_user":True,
                        "helpText":"email not is records"}, 400
            elif first_user_data and first_user_data[0]:
                return {"first_user": first_user_data[0][0]}, 200
            else:
                first_user_data.update({"first_user": True})
                return first_user_data, 400

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                "first_user": True,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500


    def flipFirstUserStatus(self, req_body):
        """function to flip first-time-user-status
        after first-time user changes password
        """
        try:
            query = "select count(*) from user_login where email = %s;"
            query_data = (
                req_body["email"],
            )
            count = db_return(query, query_data)
            if count and count[0] and count[0][0]==0:
                return {"flip":False,
                        "helpText":"email not is records"}, 400
            elif count and count[0] and count[0][0]>0:
                queries_list = ["UPDATE user_login\
                                SET first_time = NOT first_time\
                                WHERE email = %s;",]

                query_data = [(req_body["email"],),]

                res = db_no_return(queries_list, query_data)
                if  res == "success":
                    return {"flip":True}, 200
                else:
                    res.update({"flip": False})
                    return res, 500
            else:
                count.update({"flip": False})
                return count, 500


        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                "flip": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500


    def plannex_login(self, req_body):
        """function for Plannex website's login page.
        """
        try:
            query = "select count(*) from plannex_user_login where email = %s and password = %s;"
            query_data = (
                req_body["email"],
                req_body["password"],
            )
            count = db_return(query, query_data)
            if count and count[0] and count[0][0]>=1:
                return {"login":True}, 200
            elif count and count[0] and count[0][0]==0:
                return {"login":False,"helpText":"Invalid Creds"}, 200

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                "flip": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500

# obj = UserProfile()
# print(obj.signup({
#     "email": "automaizxcl3qas.petonic@gmail.com",
#     "role": "initiator",
#     "f_name": "Jitendra",
#     "l_name": "Nayak",
#     "employee_id": "NEW004",
#     "subscription_id": "RfxC5qfaff_automail.petonic@gmail.com",
#     "admin_email": "automail.petonic@gmail.com",
#     "admin_password": "xkAtdCD1"
# }))