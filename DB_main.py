"""
    this code primarily contains the funtions to connect
    python code to PostgreSQL database by calling relevant
    pyscopg2 operation files (CRUD)
"""
import sys
import json
import logging
from psycopg2 import Error
import pandas as pd
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


class DBMain:
    """
       this class primarily contains the funtions to connect
       python code to PostgreSQL database by calling relevant
       pyscopg2 operation files (CRUD)
    """
    def login(self, req_body):
        """Function for the login functionality.
           Check the count of rows after join.
        """

        try:
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


    def signup(self, req_body):
        """function for signup funtionality"""
        try:
            # Queries Formation
            first_password = utils.generate_random_string(str_len=8)

            queries_list = [
                "INSERT INTO user_login (user_id, company_id, email, password, role) VALUES (%s, %s, %s, %s, %s);",    # pylint: disable=line-too-long
                "INSERT INTO user_signup (f_name, l_name, user_id) VALUES (%s, %s, %s);",
            ]

            query_data = [
                (
                    req_body["role"] + "_" + req_body["email"],
                    req_body["company_id"],
                    req_body["email"],
                    first_password,
                    req_body["role"],
                ),
                (
                    req_body["f_name"],
                    req_body["l_name"],
                    req_body["role"] + "_" + req_body["email"],
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


    def validation(self, req_body):
        """function for email-validation funtionality
           after user signup
        """
        try:
            # Queries Formation
            queries_list = ["INSERT INTO validation (user_id) VALUES (%s);"]

            query_data = [(req_body["role"] + "_" + req_body["email"],)]

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
                WHERE user_id = %s;"
            ]

            query_data = [(new_password, req_body["role"] + "_" + req_body["email"])]

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
                WHERE user_id = %s;"
            ]

            query_data = [(req_body["new_password"], req_body["role"] + "_" + req_body["email"])]

            try:
                res = db_create_update(queries_list, query_data)
                if res == "success":   # pylint: disable=no-else-return
                    return {"reset": True}
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
        """function to check if user validated email after
           after signup. This funtion is part of stack invoked
           after user chooses forgot-password funtionality
        """

        try:
            query = "select count(*) \
                    from validation \
                    where user_id = %s;"
            query_data = (req_body["role"] + "_" + req_body["email"],)

            return db_read(query, query_data)

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
            }


    def change_password_response_from_query(self, req_body):
        """function to check if user provided valid creds
           before proceeding to set a new password for the
           corresponding account
        """

        try:
            query = "select count(*)\
                    from user_login as ul\
                    inner join validation as v\
                    on ul.user_id = v.user_id\
                    where ul.user_id = %s and ul.password = %s;"
            query_data = (
                req_body["role"] + "_" + req_body["email"],
                req_body["current_password"],
            )

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


    def change_password_main(self, req_body):
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
                    return ({"reset": True}, 201)
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


    def business_scenario_industry_dropdown(self):
        """function to fetch data for "Industry" dropdown
           under "Business Scenario tab
        """

        try:
            return db_read(query = "select * from industry_list;", query_data = None)

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
            }


    def business_scenario_domain_dropdown(self, req_body):
        """function to fetch data for "Domain" dropdown
           under "Business Scenario tab
        """

        try:
            query = "select domain_id,name\
                    from domain_list\
                    where industry_id = %s;"
            query_data = (req_body["industry_id"],)

            return db_read(query, query_data)

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
            }


    def business_scenario_process_dropdown(self, req_body):
        """function to fetch data for "Process" dropdown
           under "Business Scenario tab
        """

        try:
            query = "select process_id,name\
                        from process_list\
                        where domain_id = %s;"
            query_data = (req_body["domain_id"],)

            return db_read(query, query_data)

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
            }


    def business_scenario_complete_dropdown(self):
        """function to fetch data for all dropdowns
           under "Business Scenario tab
        """

        try:
            data_frame_data = db_read(query = "select il.name as industry,\
                                    dl.name as domain, pl.name as process\
                                    from industry_list as il\
                                    join domain_list as dl\
                                    on il.industry_id = dl.industry_id\
                                    join process_list as pl\
                                    on dl.domain_id = pl.domain_id;",
                            query_data = None)
            data_frame = pd.DataFrame(
                data_frame_data,
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
                        data_frame[(data_frame["Business"] == business) &
                                (data_frame["Domain"] == domain)]["Process"]
                    )

            return dct

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
            }


    def update_challenge_status(self, req_body):
        """function adding/updating an entry in the challenge_status table"""
        try:
            # Queries Formation
            query = [
                        "INSERT INTO challenge_status (challenge_id, challenge_status)\
                        VALUES (%s, %s)\
                        ON CONFLICT (challenge_id) DO UPDATE SET challenge_status = %s;",
                ]
            query_data = [
                            (
                                req_body["challenge_id"],
                                req_body["challenge_status"],
                                req_body["challenge_status"]
                            )
                        ]
            try:
                res = db_create_update(query, query_data)
                if res == "success":   # pylint: disable=no-else-return
                    return {"update": True}, 201
                else:
                    res.update({"update": False})
                    return res, 400

            except Exception as db_error:  # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)    # pylint: disable=line-too-long
                return {
                    "update": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "update": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500


    def fetch_challenge_status(self,req_body):
        """function fetchting an entry from the challenge_status table"""
        try:
            # Queries Formation
            query = "select challenge_status from challenge_status where challenge_id=%s;"
            query_data = (req_body["challenge_id"],)

            try:
                res = db_read(query, query_data)

                try:
                    return {"fetch": True,
                            "status": res[0][0]}, 200
                except IndexError:
                    return {"fetch": False,
                            "status": None,
                            "helpText": "challenge_id not found"}, 400

            except Exception as db_error:  # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)    # pylint: disable=line-too-long
                return {
                    "fetch": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "fetch": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500


    def update_challenge_json(self, req_body):
        """function adding/updating an entry in the challenge_json_data table"""
        try:
            # Queries Formation
            query = [
                        "INSERT INTO challenge_json_data (challenge_identifier, json_data)\
                        VALUES (%s, %s)\
                        ON CONFLICT (challenge_identifier) DO UPDATE SET json_data = %s;",
                ]
            query_data = [
                            (
                                req_body["challenge_identifier"],
                                json.dumps(req_body["json_data"]),
                                json.dumps(req_body["json_data"])
                            ),
                        ]

            try:
                res = db_create_update(query, query_data)

                if res == "success":   # pylint: disable=no-else-return
                    return {"update": True}, 201
                else:
                    res.update({"update": False})
                    return res, 400

            except Exception as db_error:  # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)    # pylint: disable=line-too-long
                return {
                    "update": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "update": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500


    def fetch_challenge_json(self, req_body):
        """function for fetchting an entry from the challenge_json_data table"""
        try:
            query = "select * from challenge_json_data where challenge_identifier=%s;"
            query_data = (req_body["challenge_identifier"],)

            try:
                res = db_read(query, query_data)

                try:
                    return {"fetch": True,
                            "json_data": res[0][1]}, 200
                except IndexError:
                    return {"fetch": False,
                            "json_data": {},
                            "helpText": "challenge_identifier not found"}, 400

            except Exception as db_error:  # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)    # pylint: disable=line-too-long
                return {
                    "fetch": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "fetch": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500


    def challenge_creation(self, req_body):
        """function for challenge creation (an entry in challenge table)"""
        try:
            # Queries Formation
            query = ["INSERT INTO challenge\
                     (challenge_id, initiator_id, date,\
                     industry, process, domain, background)\
                     VALUES (%s, %s,%s,%s,%s,%s,%s);",]
            query_data = [
                            (
                                req_body["challenge_id"],
                                req_body["initiator_id"],
                                req_body["date"],
                                req_body["industry"],
                                req_body["process"],
                                req_body["domain"],
                                req_body["background"]
                            ),
                        ]

            try:
                res = db_create_update(query, query_data)

                if res == "success":   # pylint: disable=no-else-return
                    return {"creation": True}, 201
                else:
                    logger.warning("challenge_id already present")
                    res.update({"creation": False})
                    return res, 400

            except Exception as db_error:  # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)    # pylint: disable=line-too-long
                return {
                    "creation": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "creation": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500


    def challenge_count(self, req_body):
        """function for counting the number of
           challenges corresponding to a user_id
        """
        try:
            # Queries Formation
            query = "select count(*) from challenge where initiator_id=%s;"
            query_data = (
                            req_body["initiator_id"],
                        )

            try:
                ret_data = db_read(query, query_data)

                return {"count_fetch": True,
                        "count": ret_data[0][0]}, 200

            except Exception as db_error:  # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)    # pylint: disable=line-too-long
                return {
                    "count_fetch": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "count_fetch": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",    # pylint: disable=line-too-long
            }, 500
