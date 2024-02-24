"""
    this code primarily contains the funtions related to change
    password to connect the python code to PostgreSQL database
    by calling relevant pyscopg2 operation files (CRUD)
"""
import os
import sys
import logging
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
file_handler = logging.FileHandler(os.path.join(log_directory, "change_password.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


utils = Utils()


class ChangePassword:
    """
       this class primarily contains the funtions related to change
       password to connect python code to PostgreSQL database by
       calling relevant pyscopg2 operation files (CRUD)
    """


    def change_password_execute_query(self, req_body):
        """function to excute query to set a new paasword
           to database after user chooses change-password
           funtionality
        """
        try:
            # Queries Formation
            queries_list = [
                "UPDATE user_login \
                SET password = %s \
                WHERE email = %s;"
            ]

            query_data = [(req_body["new_password"], req_body["email"])]

            try:
                res = db_no_return(queries_list, query_data)
                if res == "success":   # pylint: disable=no-else-return
                    return {"reset": True, "new_password": req_body["new_password"]}
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


    def change_password_response_from_query(self, req_body):
        """function to check if front-end provided valid creds
           before proceeding to set a new password for the
           corresponding account
        """

        try:
            query = "select count(*)\
                    from user_login as ul\
                    inner join validation as v\
                    on ul.email = v.email\
                    where ul.email = %s and ul.password = %s;"
            query_data = (
                req_body["email"],
                req_body["current_password"],
            )

            return db_return(query, query_data)

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
            }


    def change_password_main(self, req_body):             # pylint: disable=too-many-return-statements
        """function to trigger functions stack for
           change-password functionality
        """
        data = self.change_password_response_from_query(req_body)
        logger.info(data)
        # below 2 lines for testing
        # data[0] = ("qw",0)
        # data[0] = (12,0)
        if isinstance(data[0][0], int):
            if data[0][0] == 1:
                reset_action = self.change_password_execute_query(req_body)
                if reset_action["reset"]:   # pylint: disable=no-else-return
                    try:
                        logger.info(             # pylint: disable=logging-too-many-args
                            "In function: ",
                            utils.send_mail_trigger_change_pass(
                                req_body["email"], reset_action["new_password"]
                            ),
                        )
                        return ({"reset": True}, 201)
                    except Exception as mail_error3:  # pylint: disable=broad-exception-caught
                        logger.error("Failed to send mail: %s", mail_error3)
                        return ({
                                "reset": True,
                                "helpText": "failed to send mail",
                                }, 500)
                else:
                    return ({"reset": False, "helpText": "failed to reset password"}, 500)
            elif data[0][0] == 0:
                return ({
                        "reset": False,
                        "uiText": "Please enter correct current password",
                        }, 401
                        )
            else:
                reset_action = self.change_password_execute_query(req_body)
                if reset_action["reset"]:   # pylint: disable=no-else-return
                    return ({"reset": True, "IT_alert": True}, 202)
                else:
                    return ({
                            "reset": False,
                            "helpText": "failed to reset password",
                            "IT_alert": True,
                            }, 500)
        else:
            return ({"helpText": {"data": data}, "reset": False}, 500)
