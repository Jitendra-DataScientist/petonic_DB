"""
This code contains the functions related to admin
like functions to edit user details, view-list etc.
"""
import os
import sys
import logging
import json
import time
from db_return import db_return
from db_no_return import db_no_return
from user_profile import UserProfile
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
file_handler = logging.FileHandler(os.path.join(log_directory, "admin.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


user_profile_instance = UserProfile()
utils = Utils()

class Admin:
    """
    This code contains the functions related to admin
    like functions to edit user details, view-list etc.
    """

    def __init__(self):
        self.user_profile_file = "logs/user_profile.json"
        if not os.path.exists(self.user_profile_file):
            with open(self.user_profile_file, "w", encoding="utf-8") as file_handle:
                file_handle.write("{}")


    def flip_user_status(self, request_body):  # pylint: disable=too-many-return-statements)
        """
            function to deactivate or reactivate
            a particular user profile on User
            Management Page (to be done by
            admin).
        """
        try:  # pylint: disable=too-many-nested-blocks
            req_body = request_body.copy()
            req_body['email'] = req_body['email'].lower()
            req_body['admin_email'] = req_body['admin_email'].lower()
            # verify admin creds
            try:
                if user_profile_instance.login(
                    {"email":req_body["admin_email"],
                     "password":req_body["admin_password"]
                     }
                     )[1] == "admin":
                    pass
                else:
                    return {"update": False,
                            "helpText": "invalid admin creds"}, 400
            except Exception as admin_auth:  # pylint: disable=broad-exception-caught
                logger.info("admin_auth: %s", admin_auth)
                return {"update": False,
                        "helpText": "admin authorisation error"}, 500

            ## first check if mail-id present in DB
            query = "SELECT count(ul.email), v.active\
                    FROM user_login ul\
                    LEFT JOIN validation v\
                    ON (ul.email = v.email)\
                    WHERE ul.email = %s\
                    GROUP BY v.active"
            query_data = (
                req_body["email"],
            )
            ret_data = db_return(query, query_data)
            if isinstance(ret_data[0][0], int):
                if ret_data[0][0] >= 1:
                    # Queries Formation
                    queries_list = ["UPDATE validation\
                                    SET active = NOT active\
                                    WHERE email = %s;",]

                    query_data = [(req_body["email"],),]

                    try:
                        res = db_no_return(queries_list, query_data)

                        if  res == "success":   # pylint: disable=no-else-return
                            try:
                                utils.send_mail_trigger_status_change(
                                    req_body["email"], not ret_data[0][1]
                                    )
                            except Exception as mail_error:  # pylint: disable=broad-exception-caught
                                exception_type, _, exception_traceback = sys.exc_info()
                                filename = exception_traceback.tb_frame.f_code.co_filename
                                line_number = exception_traceback.tb_lineno
                                logger.error("%s||||%s||||%d", exception_type,
                                             filename, line_number)
                                return {
                                    "update": False,
                                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{mail_error}",    # pylint: disable=line-too-long
                                }
                            return {"update": True}, 200
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
                else:
                    return {"update": False,
                            "helpText": "mail-id not found in DB"}, 400
            else:
                return {"update": False,
                        "helpText": "DB error"}, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                "update": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500


    def edit_details(self, request_body):  # pylint: disable=too-many-locals,too-many-return-statements,too-many-branches,too-many-statements
        """
            function to edit first name, last name,
            employee id and/or role.
        """
        print (json.dumps(request_body,indent=4))
        # verify admin creds
        try:
            req_body = request_body.copy()
            req_body['email'] = req_body['email'].lower()
            req_body['admin_email'] = req_body['admin_email'].lower()

            if user_profile_instance.login(
                {"email":req_body["admin_email"],
                 "password":req_body["admin_password"]
                 }
                 )[1] == "admin":
                pass
            else:
                return {"update": False,
                        "helpText": "invalid admin creds"}, 400
        except Exception as admin_auth:  # pylint: disable=broad-exception-caught
            logger.info("admin_auth: %s", admin_auth)
            return {"update": False,
                    "helpText": "admin authorisation error"}, 500

        if not req_body['f_name'] and not req_body['l_name'] and\
              not req_body['role'] and not req_body['employee_id']:
            return {"update":False,
                    "helpText": "at least one of f_name, l_name,\
                        role or employee_id must be passed in payload"}, 400

        if req_body['role']:
            role_query = "select us.role, ul.subscription_id \
                    from user_signup us\
                    join user_login ul\
                    on ul.email=us.email\
                    where us.email = %s"
            role_query_data = (
                req_body["email"],
            )
            role_ret_data = db_return(role_query, role_query_data)
            if role_ret_data[0][0] == 'admin':
                role_query = "select count(*) \
                            from user_login ul\
                            join user_signup us\
                            on ul.email = us.email\
                            where ul.subscription_id = %s and us.role = %s"
                role_query_data = (
                    role_ret_data[0][1],
                    "admin",
                )
                role_ret_data = db_return(role_query, role_query_data)
                if role_ret_data[0][0] == 1:
                    return {"update":False,
                            "helpText": "This is the only admin account for this subscription_id"}, 400

        try:   # pylint: disable=too-many-nested-blocks
            ## first check if mail-id present in DB
            query = "select count(*) \
                    from user_signup\
                    where user_signup.email = %s"
            query_data = (
                req_body["email"],
            )
            ret_data = db_return(query, query_data)
            if isinstance(ret_data[0][0], int):
                if ret_data[0][0] >= 1:
                    # Filter out the None values from req_body
                    update_fields = {key: value for key, value in\
                                      req_body.items() if value is not None\
                                      and key not in ["admin_email", "admin_password"]}

                    # Construct the SET clause of the SQL query dynamically
                    set_clause = ", ".join(f"{key} = %s" for key in update_fields)

                    # Construct the WHERE clause for the email
                    where_clause = "WHERE email = %s"

                    # Construct the final SQL query
                    update_query = f"UPDATE user_signup SET {set_clause} {where_clause};"

                    # Create a tuple of values for the query
                    values = tuple(update_fields.values()) + (req_body["email"],)

                    # Now you can use these in your queries_list and query_data
                    queries_list = [update_query]
                    query_data = [values]

                    try:
                        res = db_no_return(queries_list, query_data)

                        if res == "success":   # pylint: disable=no-else-return
                            # Update user profile JSON data and send mail if role has changed
                            if "role" in update_fields:
                                # Read existing user profile data
                                with open(self.user_profile_file, "r",
                                          encoding="utf-8") as file_handle:
                                    user_profile_data = json.load(file_handle)

                                # Check if the role already exists for this email
                                if req_body["role"] in user_profile_data.get(req_body["email"], {}):
                                    # Role already exists, append the epoch to the existing list
                                    user_profile_data[req_body["email"]][req_body["role"]].append(
                                        time.time()
                                        )
                                else:
                                    # Role does not exist, create a new list with the current epoch
                                    user_profile_data.setdefault(req_body["email"], {})[
                                        req_body["role"]
                                        ] = [time.time()]

                                # Write updated user profile data back to the file
                                with open(self.user_profile_file, "w",
                                          encoding="utf-8") as file_handle:
                                    json.dump(user_profile_data, file_handle)

                                # send mail
                                try:
                                    utils.send_mail_trigger_role_change(
                                        req_body["email"], req_body["role"]
                                        )
                                except Exception as mail_error:             # pylint: disable=broad-exception-caught
                                    logger.error("Mail sending error: %s", mail_error)
                            return {"update": True}, 200
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
                else:
                    return {"update": False,
                            "helpText": "mail-id not found in DB"}, 400
            else:
                return {"update": False,
                        "helpText": "DB error"}, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                "update": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500


    def admin_view_list(self, req_body):
        """
            function to fetch details of all users
            for the admin view list.
        """
        try:
            # Queries Formation
            query = """SELECT us.email,us.role,us.employee_id,us.f_name,us.l_name,v.active
                    FROM user_signup us
                    LEFT JOIN validation v ON us.email = v.email
                    LEFT JOIN user_login ul ON ul.email = v.email
                    WHERE ul.subscription_id = %s;"""
            query_data = (
                req_body["subscription_id"],
            )
            ret_data = db_return(query, query_data)
            return {"fetch": True,
                    "data": ret_data,
                    "fields":["email", "role", "employee_id", "f_name", "l_name", "active"]}, 200

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                "fetch": False,
                "fields":["email", "role", "employee_id", "f_name", "l_name", "active"],
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500
