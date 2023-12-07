# pylint: disable=too-many-lines
"""
    this code primarily contains the funtions to connect
    python code to PostgreSQL database using pysycopg2
"""
import os
import sys
import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import json
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


class DB_psycopg2:
    def login(self, req_body):   # pylint: disable=too-many-branches
        """Function that executes (a) query (queries) and return(s) some data from the database"""

        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Query Formation
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

            # Execute the query
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


    def generate_random_string(self, str_len):
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


    def send_email(self, subject, body, to_email, sender_email, sender_password, smtp_server, image_path=None):      # pylint: disable=line-too-long,too-many-arguments
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


    def send_mail_trigger_signup(self, to_email, first_password):
        """mail sender trigger function"""
        subject = "Innovation.ai SignUp"
        try:
            logo_url = os.getenv("logo_url")
            body = (
                    f"""<p>Hello,<br>
                    An account has been created on Innovation.ai, the password for which
                    is <strong>{first_password}</strong>.<br>
                    Please log in using this password to set a new password.</p>
                    <p>If you do not recognise this activity, please ignore this email.</p>
                    <p>Best regards,<br>
                    Petonic Team</p>
                    <img src={logo_url} alt="Petonic Company Logo">"""
                )

        except Exception as mail_error:  # pylint: disable=broad-exception-caught
            logger.critical("Failed to load logo_url from .env: %s", mail_error)
            body = (
                    f"""<p>Hello,<br>
                    An account has been created on Innovation.ai, the password for which
                    is <strong>{first_password}</strong>.<br>
                    Please log in using this password to set a new password.</p>
                    <p>If you do not recognise this activity, please ignore this email.</p>
                    <p>Best regards,<br>
                    Petonic Team</p>"""
                )

        # SMTP server details
        smtp_server = "smtp.gmail.com"
        try:
            sender_email = os.getenv("sender_email")
            sender_password = os.getenv("sender_password")
        except Exception as mail_error1:     # pylint: disable=broad-exception-caught
            logger.critical("Failed to fetch auto-mail creds from env: %s", mail_error1)
            sender_email = "automail.petonic@gmail.com"
            sender_password = "efvumbcfgryjachh"

        try:
            self.send_email(subject, body, to_email, sender_email, sender_password, smtp_server)
            logger.info("mail sent !!")
            return True
        except Exception as mail_error2:   # pylint: disable=broad-exception-caught
            logger.critical("Mail sending error: %s", mail_error2)
            return False


    def signup(self, req_body):         # pylint: disable=too-many-return-statements,too-many-branches,inconsistent-return-statements,too-many-statements
        """function for processing (a) query (queries) that
        do(does) not return any response(s) from database"""
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Queries Formation
            first_password = self.generate_random_string(str_len=8)

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
                for query_count, query in enumerate(queries_list):
                    # Execute the query
                    cursor.execute(query, query_data[query_count])

                    # Print a success message
                    logger.info("Query %d executed successfully", query_count)

                # Commit the transaction
                connection.commit()

                if self.send_mail_trigger_signup(req_body["email"], first_password):          # pylint: disable=no-else-return
                    return {"user_creation": True}, 201
                else:
                    return {"user_creation": False,
                            "helpText": "Failed to send email"}, 500

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
        # except Error as e:
        #     logger.error(f"Error: {e}")

        finally:
            # Close the cursor and the database connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def validation(self, req_body):         # pylint: disable=too-many-return-statements,too-many-branches,inconsistent-return-statements,too-many-statements
        """function for processing (a) query (queries) that
        do(does) not return any response(s) from database"""
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Queries Formation
            queries_list = ["INSERT INTO validation (user_id) VALUES (%s);"]

            query_data = [(req_body["role"] + "_" + req_body["email"],)]

            try:
                for query_count, query in enumerate(queries_list):
                    # Execute the query
                    cursor.execute(query, query_data[query_count])

                    # Print a success message
                    logger.info("Query %d executed successfully", query_count)

                # Commit the transaction
                connection.commit()

                return {"validation": True}, 200

            except Exception as db_error:   # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d", exception_type, filename, line_number)
                return {
                    "validation": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}",
                }, 400

        except Exception as db_error:           # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                "validation": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}",
            }, 500
        # except Error as e:
        #     logger.error(f"Error: {e}")

        finally:
            # Close the cursor and the database connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def send_mail_trigger_forgot_pass(self, to_email, new_password):
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
                    f"""<p>Hello,<br>
                    Your password has been reset to <strong>{new_password}</strong>.<br>
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
            logger.critical("Failed to fetch auto-mail creds from env: %s", mail_error1)
            sys.exit()

        try:
            self.send_email(subject, body, to_email, sender_email, sender_password, smtp_server)
            logger.info("mail sent !!")
            return "mail sent !!"
        except Exception as mail_error2:   # pylint: disable=broad-exception-caught
            logger.critical("Mail sending error: %s", mail_error2)
            return "Mail sending error: ", mail_error2


    def validation(self, req_body):         # pylint: disable=too-many-return-statements,too-many-branches,inconsistent-return-statements,too-many-statements
        """function for processing (a) query (queries) that
        do(does) not return any response(s) from database"""
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Queries Formation
            queries_list = ["INSERT INTO validation (user_id) VALUES (%s);"]

            query_data = [(req_body["role"] + "_" + req_body["email"],)]

            try:
                for query_count, query in enumerate(queries_list):
                    # Execute the query
                    cursor.execute(query, query_data[query_count])

                    # Print a success message
                    logger.info("Query %d executed successfully", query_count)

                # Commit the transaction
                connection.commit()

                return {"validation": True}, 200

            except Exception as db_error:   # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d", exception_type, filename, line_number)
                return {
                        "validation": False,
                        "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}",
                    }, 400

        except Exception as db_error:           # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
            return {
                    "validation": False,
                    "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}",
                }, 500
        # except Error as e:
        #     logger.error(f"Error: {e}")

        finally:
            # Close the cursor and the database connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def forgot_password_execute_query(self, req_body):         # pylint: disable=too-many-return-statements,too-many-branches,inconsistent-return-statements,too-many-statements
        """function for processing (a) query (queries) that
        do(does) not return any response(s) from database"""
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Queries Formation
            new_password = self.generate_random_string(str_len=8)
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

                return {"reset": True, "new_password": new_password}

            except Exception as db_error:   # pylint: disable=broad-exception-caught
                exception_type, _, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                logger.error("%s||||%s||||%d", exception_type, filename, line_number)
                return {
                        "reset": False,
                        "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}",
                    }

        except Exception as db_error:           # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
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
                        "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}",
                    }

        except Exception as db_error:           # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%d", exception_type, filename, line_number)
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


    def forgot_password_response_from_query(self, req_body):   # pylint: disable=too-many-branches
        """Function that executes (a) query (queries) and return(s) some data from the database"""

        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Query Formation
            query = "select count(*) \
                    from validation \
                    where user_id = %s;"
            query_data = (req_body["role"] + "_" + req_body["email"],)

            # Execute the query
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


    def change_password_response_from_query(self, req_body):   # pylint: disable=too-many-branches
        """Function that executes (a) query (queries) and return(s) some data from the database"""

        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Query Formation
            query = "select count(*)\
                        from user_login as ul\
                        inner join validation as v\
                        on ul.user_id = v.user_id\
                        where ul.user_id = %s and ul.password = %s;"
            query_data = (
                req_body["role"] + "_" + req_body["email"],
                req_body["current_password"],
            )

            # Execute the query
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


    def business_scenario_industry_dropdown(self):   # pylint: disable=too-many-branches
        """Function that executes (a) query (queries) and return(s) some data from the database"""

        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Query Formation
            query = "select *\
                        from industry_list;"

            # Execute the query
            cursor.execute(query)

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


    def business_scenario_domain_dropdown(self, req_body):   # pylint: disable=too-many-branches
        """Function that executes (a) query (queries) and return(s) some data from the database"""

        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Query Formation
            query = "select domain_id,name\
                        from domain_list\
                        where industry_id = %s;"
            query_data = (req_body["industry_id"],)

            # Execute the query
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


    def business_scenario_process_dropdown(self, req_body):   # pylint: disable=too-many-branches
        """Function that executes (a) query (queries) and return(s) some data from the database"""

        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Query Formation
            query = "select process_id,name\
                        from process_list\
                        where domain_id = %s;"
            query_data = (req_body["domain_id"],)

            # Execute the query
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


    def business_scenario_complete_dropdown(self):   # pylint: disable=too-many-branches
        """Function that executes (a) query (queries) and return(s) some data from the database"""

        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Query Formation
            query = "select il.name as industry, dl.name as domain, pl.name as process\
                    from industry_list as il\
                    join domain_list as dl\
                    on il.industry_id = dl.industry_id\
                    join process_list as pl\
                    on dl.domain_id = pl.domain_id;"

            # Execute the query
            cursor.execute(query)

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