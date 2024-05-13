"""
    this code primarily contains the
    functions related to subscription
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
file_handler = logging.FileHandler(os.path.join(log_directory, "subscription.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


utils = Utils()


class Subscription:
    """
        this class primarily contains the
        functions related to subscription
    """


    def firstAdd(self, req_body):
        """Function for adding basic
           subscription details
        """

        try:
            subscription_id = utils.generate_random_string(str_len=10) + '_' + req_body["email"]
            otp = utils.generate_random_string(str_len=10)
            query_list = [
                """INSERT INTO subscription (
                    subscription_id,
                    plan,
                    users_count,
                    company_name,
                    phone,
                    f_name,
                    l_name,
                    email,
                    country,
                    address_line1,
                    address_line2,
                    otp
                ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            ]

            query_data = [
                (
                    subscription_id,
                    req_body["plan"],
                    req_body["users_count"],
                    req_body["company_name"],
                    req_body["phone"],
                    req_body["f_name"],
                    req_body["l_name"],
                    req_body["email"],
                    req_body["country"],
                    req_body["address_line1"],
                    req_body["address_line2"],
                    otp
                )
            ]

            # Fetch data
            res = db_no_return(query_list, query_data)

            if res == "success":   # pylint: disable=no-else-return
                if utils.subscription_mail_verify(req_body["email"], otp):
                    return {"creation": True,
                            "subscription_id": subscription_id}, 201
                else:
                    return {"creation": False,
                            "helpText": "Failed to send email"}, 500
            else:
                res.update({"creation": False})
                return res, 400

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
            }, 500


    def verifyOTP(self, req_body):
        """Function for otp verification"""

        try:
            query = "select otp \
                    from subscription\
                    where subscription_id = %s;"
            query_data = (
                req_body["subscription_id"],
            )

            otp_data = db_return(query, query_data)
            if otp_data and otp_data[0] and otp_data[0][0]==req_body["otp"]:
                query = ["""
                            UPDATE subscription
                            SET otp = 'verified'
                            WHERE subscription_id = %s
                            """]
                query_data = [(req_body["subscription_id"],),]
                update_res = db_no_return(query, query_data)
                return {"validation": True,"update_res":update_res}, 200
            elif otp_data and otp_data[0] and (otp_data[0][0]!=req_body["otp"] and otp_data[0][0]!='verified'):
                return {"validation": False,
                        "helpText":"incorrect OTP"}, 403
            elif otp_data and otp_data[0] and otp_data[0][0]=='verified':
                return {"validation": False,
                        "helpText":"mail already verified"}, 400
            else:
                return {"validation": False}, 403

        except Exception as db_error:  # pylint: disable=broad-exception-caught
            exception_type, _, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("%s||||%s||||%s", exception_type, filename, line_number)
            return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{db_error}"    # pylint: disable=line-too-long
            }, 500
