"""
This code contains the functions related to admin
like functions to edit user details, view-list etc.
"""
import sys
import logging
import json
from db_read import db_read
from db_create_update import db_create_update
from utils import Utils


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

# Create a logger instance
logger = logging.getLogger(__name__)


utils = Utils()

class Admin:
    """
    This code contains the functions related to admin
    like functions to edit user details, view-list etc.
    """
    def flip_user_status(self, req_body):
        """
            function to deactivate or reactivate
            a particular user profile on User
            Management Page (to be done by
            admin).
        """
        try:
            ## first check if mail-id present in DB
            query = "select count(*) \
                    from user_login\
                    where user_login.email = %s"
            query_data = (
                req_body["email"],
            )
            ret_data = db_read(query, query_data)
            if isinstance(ret_data[0][0], int):
                if ret_data[0][0] >= 1:
                    # Queries Formation
                    queries_list = ["UPDATE validation\
                                    SET active = NOT active\
                                    WHERE email = %s;",]

                    query_data = [(req_body["email"],),]

                    try:
                        res = db_create_update(queries_list, query_data)

                        if  res == "success":   # pylint: disable=no-else-return
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


    def edit_details(self, req_body):  # pylint: disable=too-many-locals,too-many-return-statements
        """
            function to edit first name, last name,
            employee id and/or role.
        """
        print (json.dumps(req_body,indent=4))
        if not req_body['f_name'] and not req_body['l_name'] and\
              not req_body['role'] and not req_body['employee_id']:
            return {"update":False,
                    "helpText": "at least one of f_name, l_name,\
                        role or employee_id must be passed in payload"}, 400

        try:
            ## first check if mail-id present in DB
            query = "select count(*) \
                    from user_signup\
                    where user_signup.email = %s"
            query_data = (
                req_body["email"],
            )
            ret_data = db_read(query, query_data)
            if isinstance(ret_data[0][0], int):
                if ret_data[0][0] >= 1:
                    # Filter out the None values from req_body
                    update_fields = {key: value for key, value in\
                                      req_body.items() if value is not None}

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
                        res = db_create_update(queries_list, query_data)

                        if  res == "success":   # pylint: disable=no-else-return
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


    def admin_view_list(self):
        """
            function to fetch details of all users
            for the admin view list.
        """
        try:
            # Queries Formation
            query = "SELECT us.email,us.role,us.employee_id,us.f_name,us.l_name,v.active\
                    FROM user_signup us\
                    LEFT JOIN validation v ON us.email = v.email;"
            query_data = None
            ret_data = db_read(query, query_data)
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
