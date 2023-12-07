# pylint: disable=too-many-lines
"""
    this code primarily contains the funtions to connect
    python code to PostgreSQL database using pysycopg2
"""
import os
import sys
import json
import logging
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
from DB_read import DB_read
from DB_create import DB_create
from DB_update import DB_update
from utils import utils


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


DB_read_inst = DB_read()
DB_create_inst = DB_create()
DB_update_inst = DB_update()
utils = utils()


class DB_main:
    def login(self, req_body):   # pylint: disable=too-many-branches
        """Function that executes (a) query (queries) and return(s) some data from the database"""

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
            ret_data = DB_read_inst.db_read(query,query_data)

            return ret_data

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"
            }


    def signup(self, req_body):         # pylint: disable=too-many-return-statements,too-many-branches,inconsistent-return-statements,too-many-statements
        """function for processing (a) query (queries) that
        do(does) not return any response(s) from database"""
        try:
            # Queries Formation
            first_password = utils.generate_random_string(str_len=8)

            queries_list = [
                "INSERT INTO user_login (user_id, company_id, email, password, role) VALUES (%s, %s, %s, %s, %s);",  # pylint: disable=line-too-long
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
                res, status_code = DB_create_inst.db_create(queries_list,query_data)

                if  status_code == 200:
                    if utils.send_mail_trigger_signup(req_body["email"], first_password):          # pylint: disable=no-else-return
                        return {"user_creation": True}, 201
                    else:
                        return {"user_creation": False,
                                "helpText": "Failed to send email"}, 500
                else:
                    res.update({"user_creation": False})
                    return res, status_code

            except Exception as db_error:   # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d", exception_type, filename, line_number)
                return {
                    "user_creation": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",   # pylint: disable=line-too-long
                }, 400

        except Exception as db_error:           # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                "user_creation": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",   # pylint: disable=line-too-long
            }, 500


    def validation(self, req_body):         # pylint: disable=too-many-return-statements,too-many-branches,inconsistent-return-statements,too-many-statements
        """function for processing (a) query (queries) that
        do(does) not return any response(s) from database"""
        try:
            # Queries Formation
            queries_list = ["INSERT INTO validation (user_id) VALUES (%s);"]

            query_data = [(req_body["role"] + "_" + req_body["email"],)]

            try:
                res, status_code = DB_create_inst.db_create(queries_list,query_data)

                if  status_code == 200:
                    return {"validation": True}, 200
                else:
                    res.update({"validation": False})
                    return res, status_code

            except Exception as db_error:   # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d", exception_type, filename, line_number)
                return {
                    "validation": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",
                }, 400

        except Exception as db_error:           # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                "validation": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",
            }, 500


    def forgot_password_execute_query(self, req_body):         # pylint: disable=too-many-return-statements,too-many-branches,inconsistent-return-statements,too-many-statements
        """function for processing (a) query (queries) that
        do(does) not return any response(s) from database"""
        try:
            new_password = utils.generate_random_string(str_len=8)
            queries_list = [    
                "UPDATE user_login \
                SET password = %s \
                WHERE user_id = %s;"
            ]

            query_data = [(new_password, req_body["role"] + "_" + req_body["email"])]

            try:
                res = DB_update_inst.db_update(queries_list, query_data)

                if res == "success":
                    return {"reset": True, "new_password": new_password}
                else:
                    res.update({"reset": False})
                    return res

            except Exception as db_error:   # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d", exception_type, filename, line_number)
                return {
                        "reset": False,
                        "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",
                    }

        except Exception as db_error:           # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                    "reset": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",
                }


    def change_password_execute_query(self, req_body):         # pylint: disable=too-many-return-statements,too-many-branches,inconsistent-return-statements,too-many-statements
        """function for processing (a) query (queries) that
        do(does) not return any response(s) from database"""
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Queries Formation
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

                return {"reset": True}

            except Exception as db_error:   # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d", exception_type, filename, line_number)
                return {
                        "reset": False,                  # pylint: disable=line-too-long
                        "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",
                    }

        except Exception as db_error:           # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                    "reset": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",
                }

        finally:
            # Close the cursor and the database connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def forgot_password_response_from_query(self, req_body):   # pylint: disable=too-many-branches
        """Function that executes (a) query (queries) and return(s) some data from the database"""

        try:
            query = "select count(*) \
                    from validation \
                    where user_id = %s;"
            query_data = (req_body["role"] + "_" + req_body["email"],)

            return DB_read_inst.db_read(query,query_data)

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"
            }


    def change_password_response_from_query(self, req_body):   # pylint: disable=too-many-branches
        """Function that executes (a) query (queries) and return(s) some data from the database"""

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

            return DB_read_inst.db_read(query, query_data)

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"
            }


    def forgot_password_main(self, req_body):
        data = self.forgot_password_response_from_query(req_body)
        logger.info(data)
        # below 2 lines for testing
        # data[0] = ("qw",0)
        # data[0] = (12,0)
        if isinstance(data[0][0], int):
            if data[0][0] == 1:
                reset_action = self.forgot_password_execute_query(req_body)
                print (reset_action)
                if reset_action["reset"]:
                    try:
                        logger.info(                 # pylint: disable=logging-too-many-args
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
                                },500 )
                else:
                    return ({
                            "reset_link": False,
                            "helpText": "failed to generate password",
                            },500)
            elif data[0][0] == 0:
                return ({"reset_link": False, "uiText": "Unidentified email ID"},401)
            else:
                reset_action = self.forgot_password_execute_query(req_body)
                if reset_action["reset"]:
                    try:
                        logger.info(
                                    "In function: send_mail_trigger_forgot_pass(email=%s, new_password=%s) returned: %s",       # pylint: disable=line-too-long
                                    req_body["email"],
                                    reset_action["new_password"],
                                    utils.send_mail_trigger_forgot_pass(req_body["email"], reset_action["new_password"]),       # pylint: disable=line-too-long
                                )

                        return ({"reset_link": True, "IT_alert": True}, 202)
                    except Error as mail_error4:
                        logger.error("Failed to send mail: %s", mail_error4)
                        return ({
                                "reset_link": False,
                                "helpText": "failed to send mail",
                                "IT_alert": True,
                                },500
                                )
                else:
                    return ({
                            "reset_link": False,
                            "helpText": "failed to generate password",
                            "IT_alert": True,
                            },500,
                            )
        else:
            return (
                {"helpText": {"data": data}, "reset_link": False}, 500
                )


    def change_password_main(self, req_body):
        data = self.change_password_response_from_query(req_body)
        logger.info(data)
        # below 2 lines for testing
        # data[0] = ("qw",0)
        # data[0] = (12,0)
        if isinstance(data[0][0], int):
            if data[0][0] == 1:
                reset_action = self.change_password_execute_query(req_body)
                if reset_action["reset"]:                 # pylint: disable=no-else-return
                    return ({"reset": True}, 201)
                else:
                    return ({"reset": False, "helpText": "failed to reset password"},500)
            elif data[0][0] == 0:
                return ({
                        "reset": False,
                        "uiText": "Please enter correct current password",
                        },401
                    )
            else:
                reset_action = self.change_password_execute_query(req_body)
                if reset_action["reset"]:                 # pylint: disable=no-else-return
                    return ({"reset": True, "IT_alert": True}, 202)
                else:
                    return ({
                            "reset": False,
                            "helpText": "failed to reset password",
                            "IT_alert": True,
                            },500)
        else:
            return ({"helpText": {"data": data}, "reset": False}, 500)


    def business_scenario_industry_dropdown(self):   # pylint: disable=too-many-branches
        """Function that executes (a) query (queries) and return(s) some data from the database"""

        try:
            return DB_read_inst.db_read(query = "select * from industry_list;", query_data = None)

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"
            }


    def business_scenario_domain_dropdown(self, req_body):   # pylint: disable=too-many-branches
        """Function that executes (a) query (queries) and return(s) some data from the database"""

        try:
            query = "select domain_id,name\
                    from domain_list\
                    where industry_id = %s;"
            query_data = (req_body["industry_id"],)

            return DB_read_inst.db_read(query, query_data)

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"
            }


    def business_scenario_process_dropdown(self, req_body):   # pylint: disable=too-many-branches
        """Function that executes (a) query (queries) and return(s) some data from the database"""

        try:
            query = "select process_id,name\
                        from process_list\
                        where domain_id = %s;"
            query_data = (req_body["domain_id"],)

            return DB_read_inst.db_read(query, query_data)

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"
            }


    def business_scenario_complete_dropdown(self):   # pylint: disable=too-many-branches
        """Function that executes (a) query (queries) and return(s) some data from the database"""

        try:
            return DB_read_inst.db_read(query = "select il.name as industry, dl.name as domain, pl.name as process\
                                                from industry_list as il\
                                                join domain_list as dl\
                                                on il.industry_id = dl.industry_id\
                                                join process_list as pl\
                                                on dl.domain_id = pl.domain_id;",
                                        query_data = None)

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"
            }


    def update_challenge_status(self,req_body):
        """function adding/updating an entry in the challenge_status table"""
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Queries Formation
            query = "INSERT INTO challenge_status (challenge_id, challenge_status)\
                    VALUES (%s, %s)\
                    ON CONFLICT (challenge_id) DO UPDATE SET challenge_status = %s;"
            query_data = (req_body["challenge_id"], req_body["challenge_status"], req_body["challenge_status"])   # pylint: disable=line-too-long

            try:
                # Execute the query
                cursor.execute(query, query_data)

                # Print a success message
                logger.info("Query executed successfully")

                # Commit the transaction
                connection.commit()

                return {"update": True}, 201

            except Exception as db_error:       # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
                return {
                    "update": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",   # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:       # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "update": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",
            }, 500
        # except Error as e:
        #     logger.error(f"Error: {e}")

        finally:
            # Close the cursor and the database connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def fetch_challenge_status(self,req_body):
        """function fetchting an entry from the challenge_status table"""
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Queries Formation
            query = "select challenge_status from challenge_status where challenge_id=%s;"
            query_data = (req_body["challenge_id"],)

            try:
                # Execute the query
                cursor.execute(query, query_data)

                # Print a success message
                logger.info("Query executed successfully")

                # Commit the transaction
                connection.commit()

                try:
                    return {"fetch": True,
                            "status": cursor.fetchall()[0][0]}, 200
                except IndexError:
                    return {"fetch": False,
                            "status": None,
                            "helpText": "challenge_id not found"}, 400

            except Exception as db_error:       # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
                return {
                    "fetch": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",   # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:       # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "fetch": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",
            }, 500
        # except Error as e:
        #     logger.error(f"Error: {e}")

        finally:
            # Close the cursor and the database connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def update_challenge_json(self, req_body):
        """function adding/updating an entry in the challenge_json_data table"""
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Queries Formation
            query = "INSERT INTO challenge_json_data (challenge_identifier, json_data)\
                        VALUES (%s, %s)\
                        ON CONFLICT (challenge_identifier) DO UPDATE SET json_data = %s;"
            query_data = (
                            req_body["challenge_identifier"],
                            json.dumps(req_body["json_data"]),
                            json.dumps(req_body["json_data"])
                        )

            try:
                # Execute the query
                cursor.execute(query, query_data)

                # Print a success message
                logger.info("Query executed successfully")

                # Commit the transaction
                connection.commit()

                return {"update": True}, 201

            except Exception as db_error:       # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
                return {
                    "update": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",   # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:       # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "update": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",
            }, 500
        # except Error as e:
        #     logger.error(f"Error: {e}")

        finally:
            # Close the cursor and the database connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def fetch_challenge_json(self, req_body):
        """function fetchting an entry from the challenge_status table"""
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Queries Formation
            query = "select * from challenge_json_data where challenge_identifier=%s;"
            query_data = (req_body["challenge_identifier"],)

            try:
                # Execute the query
                cursor.execute(query, query_data)

                # Print a success message
                logger.info("Query executed successfully")

                # Commit the transaction
                connection.commit()

                try:
                    return {"fetch": True,
                            "json_data": cursor.fetchall()[0][1]}, 200
                except IndexError:
                    return {"fetch": False,
                            "json_data": {},
                            "helpText": "challenge_identifier not found"}, 400

            except Exception as db_error:       # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
                return {
                    "fetch": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",   # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:       # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "fetch": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",
            }, 500
        # except Error as e:
        #     logger.error(f"Error: {e}")

        finally:
            # Close the cursor and the database connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def challenge_creation(self,req_body):
        """function for challenge creation (an entry in challenge table)"""
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Queries Formation
            query = "INSERT INTO challenge\
                    (challenge_id, initiator_id, date, industry, process, domain, background)\
                    VALUES (%s, %s,%s,%s,%s,%s,%s);"
            query_data = (
                            req_body["challenge_id"],
                            req_body["initiator_id"],
                            req_body["date"],
                            req_body["industry"],
                            req_body["process"],
                            req_body["domain"],
                            req_body["background"]
                        )

            try:
                # Execute the query
                try:
                    cursor.execute(query, query_data)
                except psycopg2.errors.UniqueViolation:           # pylint: disable=no-member
                    logger.warning("challenge_id already present")
                    return {"creation": False,
                            "helpText": "challenge_id already present"}, 400

                # Print a success message
                logger.info("Query executed successfully")

                # Commit the transaction
                connection.commit()

                return {"creation": True}, 201

            except Exception as db_error:       # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
                return {
                    "creation": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",   # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:       # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "creation": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",
            }, 500
        # except Error as e:
        #     logger.error(f"Error: {e}")

        finally:
            # Close the cursor and the database connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def challenge_count(self, req_body):
        """function for counting the number of challenges corresponding to a user_id"""
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Queries Formation
            query = "select count(*) from challenge where initiator_id=%s;"
            query_data = (
                            req_body["initiator_id"],
                        )

            try:
                # Execute the query
                cursor.execute(query, query_data)

                # Print a success message
                logger.info("Query executed successfully")

                # Commit the transaction
                connection.commit()

                # Fetch data
                ret_data = cursor.fetchall()

                return {"count_fetch": True,
                        "count": ret_data[0][0]}, 200

            except Exception as db_error:       # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
                return {
                    "count_fetch": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",   # pylint: disable=line-too-long
                }, 500

        except Exception as db_error:       # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d||||%d", exception_type, filename, line_number, db_error)
            return {
                "count_fetch": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}",
            }, 500
        # except Error as e:
        #     logger.error(f"Error: {e}")

        finally:
            # Close the cursor and the database connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()