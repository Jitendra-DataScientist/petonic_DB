"""
    this code primarily contains the funtions related to forgot
    password to connect the python code to PostgreSQL database
    by calling relevant pyscopg2 operation files (CRUD)
"""
import sys
import logging
from psycopg2 import Error
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


class ForgotPassword:
    """
       this class primarily contains the funtions related to forgot
       password to connect python code to PostgreSQL database by
       calling relevant pyscopg2 operation files (CRUD)
    """

    def forgot_password_execute_query(self, req_body):
        """function to excute query to set a new paasword
           to database after user chooses forgot-password
           funtionality
        """
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
                    return {"reset": True, "new_password": new_password}
                else:
                    res.update({"reset": False})
                    return res

            except Exception as db_error:  # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d", exception_type, filename, line_number)
                return {
                        "reset": False,
                        "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                    }

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                    "reset": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                }


    def forgot_password_response_from_query(self, req_body):
        """function to check if front-end provided valid creds
           before proceeding to set a new password for the
           corresponding account
        """

        try:
            query = "select count(*) \
                    from validation \
                    where email = %s;"
            query_data = (req_body["email"],)

            return db_read(query, query_data)

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
            }


    def forgot_password_main(self, req_body):  # pylint: disable=too-many-return-statements
        """function to trigger functions stack for
           forgot-password functionality
        """
        data = self.forgot_password_response_from_query(req_body)
        logger.info(data)
        # below 2 lines for testing
        # data[0] = ("qw",0)
        # data[0] = (12,0)
        if isinstance(data[0][0], int):
            if data[0][0] == 1:
                reset_action = self.forgot_password_execute_query(req_body)
                print(reset_action)
                if reset_action["reset"]:
                    try:
                        logger.info(             # pylint: disable=logging-too-many-args
                            "In function: ",
                            utils.send_mail_trigger_forgot_pass(
                                req_body["email"], reset_action["new_password"]
                            ),
                        )
                        return ({"reset_link": True}, 201)
                    except Error as mail_error3:
                        logger.error("Failed to send mail: %s", mail_error3)
                        return ({
                                "reset_link": False,
                                "helpText": "failed to send mail",
                                }, 500)
                else:
                    return ({
                            "reset_link": False,
                            "helpText": "failed to generate password",
                            }, 500)
            elif data[0][0] == 0:
                return ({"reset_link": False, "uiText": "Unidentified email ID"}, 401)
            else:
                reset_action = self.forgot_password_execute_query(req_body)
                if reset_action["reset"]:
                    try:
                        logger.info(
                                    "In function: send_mail_trigger_forgot_pass(email=%s, new_password=%s) returned: %s",    # pylint: disable=line-too-long
                                    req_body["email"],
                                    reset_action["new_password"],
                                    utils.send_mail_trigger_forgot_pass(req_body["email"], reset_action["new_password"]),    # pylint: disable=line-too-long
                                )

                        return ({"reset_link": True, "IT_alert": True}, 202)
                    except Error as mail_error4:
                        logger.error("Failed to send mail: %s", mail_error4)
                        return ({
                                "reset_link": False,
                                "helpText": "failed to send mail",
                                "IT_alert": True,
                                }, 500
                                )
                else:
                    return ({
                            "reset_link": False,
                            "helpText": "failed to generate password",
                            "IT_alert": True,
                            }, 500,
                            )
        else:
            return (
                {"helpText": {"data": data}, "reset_link": False}, 500
                )
