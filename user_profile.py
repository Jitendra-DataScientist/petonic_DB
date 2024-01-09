"""
    this code primarily contains the user profile funtions for
    connecting to python code to PostgreSQL database by calling
    relevant pyscopg2 operation files (CRUD)
"""
import sys
import logging
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


class UserProfile:
    """
       this class primarily contains the user profile funtions
       to connect python code to PostgreSQL database by
       calling relevant pyscopg2 operation files (CRUD)
    """
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
            ret_data = db_read(query, query_data)

            return ret_data

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
            }


    def login_trigger(self, req_body):
        """Function to trigger above login
           funtion, and return response
        """

        try:
            data = self.login(req_body)
            logger.info(data)
            # below 2 lines for testing
            # data[0] = ("qw",0)
            # data[0] = (12,0)
            if isinstance(data[0][0], int):
                if data[0][0] == 1:                  # pylint: disable=no-else-return
                    return {"login": True}, 200
                elif data[0][0] == 0:
                    return {"login": False}, 401
                else:
                    return {"login": True, "IT_alert": True}, 202
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


    def signup(self, req_body):
        """function for signup funtionality"""
        try:
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
                res = db_create_update(queries_list, query_data)

                if  res == "success":
                    if utils.send_mail_trigger_signup(req_body["email"], first_password):   # pylint: disable=no-else-return
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


    def resend_mail_signup(self, req_body):
        """funtionality to resend signup mail with a
           different password, rest creds remain the same"""
        try:
            new_password = utils.generate_random_string(str_len=8)
            queries_list = [
                "UPDATE user_login \
                SET password = %s \
                WHERE email = %s;"
            ]

            query_data = [(new_password, req_body["email"])]

            try:
                res = db_create_update(queries_list, query_data)

                if res == "success":   # pylint: disable=no-else-return
                    if utils.send_mail_trigger_signup(req_body["email"], new_password):      # pylint: disable=no-else-return
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


    def validation(self, req_body):
        """function for email-validation funtionality
           after user signup
        """
        try:
            # Queries Formation
            queries_list = ["INSERT INTO validation (email, active) VALUES (%s, %s);"]

            query_data = [(req_body["email"], True)]

            try:
                res = db_create_update(queries_list, query_data)

                if  res == "success":   # pylint: disable=no-else-return
                    return {"validation": True}, 200
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
