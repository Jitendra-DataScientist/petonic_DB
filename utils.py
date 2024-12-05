"""
    utilities other than the database related
    like random string generator, send mail etc.
"""
import os
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import random
import string
import smtplib
import logging
import threading
from dotenv import load_dotenv


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
file_handler = logging.FileHandler(os.path.join(log_directory, "utils.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


# CAUTION : the python script and .env file
# need to be in the same path for below line.
dotenv_path = os.path.join(os.getcwd(), ".env")
# below dotenv_path for local test in Downloads folder
# dotenv_path = os.path.join(os.path.expanduser("~"), "Downloads", ".env")
load_dotenv(dotenv_path)


class Utils:
    """this class has the attributes for utilites used
       in APIs other than the DB related ones
    """
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


    def send_email(self, subject, body, to_email, sender_email,            # pylint: disable=too-many-arguments
                   sender_password, smtp_server, image_path=None):
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


    def send_mail_trigger_signup(self, to_email, first_password, role):
        """mail sender trigger function"""

        subject = "SolvAI SignUp"
        body = (
                f"""<p>Hello,<br>
                An account with <strong>{role}</strong> role has been created on SolvAI,
                the user ID for which is your mail ID and password for which is <strong>
                {first_password}</strong>.<br> Please log in using these credentials.</p>
                <p>If you do not recognise this activity, please ignore this email.</p>
                <p><small><i>This is a system generated mail and doesn't require any reply or acknowledgement.</i></small></p>"""
            )

        # SMTP server details
        smtp_server = "smtp.gmail.com"
        try:
            sender_email = os.getenv("sender_email")
            sender_password = os.getenv("sender_password")
        except FileNotFoundError as file_error:
            logger.critical("Failed to fetch auto-mail creds from env: %s", file_error)
            sys.exit()

        try:
            self.send_email(subject, body, to_email, sender_email,
                            sender_password, smtp_server)
            logger.info("mail sent !!")
            return True
        except Exception as mail_error2:             # pylint: disable=broad-exception-caught
            logger.critical("Mail sending error: %s", mail_error2)
            return False


    def send_mail_trigger_forgot_pass(self, to_email, new_password):
        """mail sender trigger function"""

        subject = "Password Reset"
        body = (
                f"""<p>Hello,<br>
                Your password has been reset to <strong>{new_password}</strong>.<br>
                Please log in using this password to reset your password.</p>
                <p><small><i>This is a system generated mail and doesn't require any reply or acknowledgement.</i></small></p>"""
            )

        # SMTP server details
        smtp_server = "smtp.gmail.com"
        try:
            sender_email = os.getenv("sender_email")
            sender_password = os.getenv("sender_password")
        except FileNotFoundError as file_error:
            logger.critical("Failed to fetch auto-mail creds from env: %s", file_error)
            sys.exit()

        try:
            self.send_email(subject, body, to_email, sender_email,
                            sender_password, smtp_server)
            logger.info("mail sent !!")
            return "mail sent !!"
        except Exception as mail_error:             # pylint: disable=broad-exception-caught
            logger.critical("Mail sending error: %s", mail_error)
            return "Mail sending error: ", mail_error


    def send_mail_trigger_change_pass(self, to_email, new_password):
        """mail sender trigger function"""

        subject = "Password Reset"
        body = (
                f"""<p>Hello,<br>
                Your password has been changed to <strong>{new_password}
                </strong> successfully.<br>
                Please log in using this password now.
                If you do not recognize this activity, contact your admin.
                </p>
                <p><small><i>This is a system generated mail and doesn't require any reply or acknowledgement.</i></small></p>"""
            )

        # SMTP server details
        smtp_server = "smtp.gmail.com"
        try:
            sender_email = os.getenv("sender_email")
            sender_password = os.getenv("sender_password")
        except FileNotFoundError as file_error:
            logger.critical("Failed to fetch auto-mail creds from env: %s", file_error)
            sys.exit()

        try:
            self.send_email(subject, body, to_email, sender_email,
                            sender_password, smtp_server)
            logger.info("mail sent !!")
            return "mail sent !!"
        except Exception as mail_error:             # pylint: disable=broad-exception-caught
            logger.critical("Mail sending error: %s", mail_error)
            return "Mail sending error: ", mail_error


    def send_mail_trigger_role_change(self, to_email, role):
        """mail sender trigger function"""

        subject = "Change of Role"
        body = (
                f"""<p>Hello,<br>
                Your role for SolvAI has now been set to <strong>{role}</strong>.<br></p>
                <p><small><i>This is a system generated mail and doesn't require any reply or acknowledgement.</i></small></p>"""
            )

        # SMTP server details
        smtp_server = "smtp.gmail.com"
        try:
            sender_email = os.getenv("sender_email")
            sender_password = os.getenv("sender_password")
        except FileNotFoundError as file_error:
            logger.critical("Failed to fetch auto-mail creds from env: %s", file_error)
            sys.exit()

        try:
            self.send_email(subject, body, to_email, sender_email,
                            sender_password, smtp_server)
            logger.info("mail sent !!")
            return "mail sent !!"
        except Exception as mail_error:             # pylint: disable=broad-exception-caught
            logger.critical("Mail sending error: %s", mail_error)
            return "Mail sending error: ", mail_error


    def send_mail_trigger_status_change(self, to_email, status):
        """mail sender trigger function"""

        if status:
            subject = "Account Activated"
            body = (
                    """<p>Hello,<br>
                    Your account for SolvAI has now been activated.<br></p>
                    <p><small><i>This is a system generated mail and doesn't require any reply or acknowledgement.</i></small></p>"""
                )
        else:
            subject = "Account Deactivated"
            body = (
                    """<p>Hello,<br>
                    Your account for SolvAI has now been deactivated.<br></p>
                    <p><small><i>This is a system generated mail and doesn't require any reply or acknowledgement.</i></small></p>"""
                )
        # SMTP server details
        smtp_server = "smtp.gmail.com"
        try:
            sender_email = os.getenv("sender_email")
            sender_password = os.getenv("sender_password")
        except FileNotFoundError as file_error:
            logger.critical("Failed to fetch auto-mail creds from env: %s", file_error)
            sys.exit()

        try:
            self.send_email(subject, body, to_email, sender_email,
                            sender_password, smtp_server)
            logger.info("mail sent !!")
            return "mail sent !!"
        except Exception as mail_error:             # pylint: disable=broad-exception-caught
            logger.critical("Mail sending error: %s", mail_error)
            return "Mail sending error: ", mail_error


    def send_mail_trigger_ch_init(self, to_email, challenge_id, industry, process, domain):             # pylint: disable=too-many-arguments
        """mail sender trigger function for challenge initiation"""

        subject = "Challenge Initiated !!"
        body = (
                f"""<p>Hello,<br>
                You have successfully initiated a challenge. Please find the details
                of the challenge below:<br>
                <strong>Challenge ID: </strong>{challenge_id}<br>
                <strong>Industry: </strong>{industry}<br>
                <strong>Domain: </strong>{domain}<br>
                <strong>Process: </strong>{process}<br>
                <br></p>
                <p><small><i>This is a system generated mail and doesn't require any reply or acknowledgement.</i></small></p>"""
            )

        # SMTP server details
        smtp_server = "smtp.gmail.com"
        try:
            sender_email = os.getenv("sender_email")
            sender_password = os.getenv("sender_password")
        except FileNotFoundError as file_error:
            logger.critical("Failed to fetch auto-mail creds from env: %s", file_error)
            sys.exit()

        try:
            self.send_email(subject, body, to_email, sender_email,
                            sender_password, smtp_server)
            logger.info("mail sent !!")
            return "mail sent !!"
        except Exception as mail_error:             # pylint: disable=broad-exception-caught
            logger.critical("Mail sending error: %s", mail_error)
            return "Mail sending error: ", mail_error


    def send_mail_trigger_ch_sub(self, to_email, challenge_id, name, description, cont_list):             # pylint: disable=too-many-arguments
        """mail sender trigger function for challenge submission (initiator mail)"""

        subject = "Challenge Submitted !!"
        body = (
                f"""<p>Hello,<br>
                You have successfully submitted a challenge. Please find the details
                of the challenge below:<br>
                <strong>Challenge ID: </strong>{challenge_id}<br>
                <strong>Challenge Name: </strong>{name}<br>
                <strong>Challenge Description: </strong>{description}<br>
                <br></p>
                <p><small><i>This is a system generated mail and doesn't require any reply or acknowledgement.</i></small></p>"""
            )

        # SMTP server details
        smtp_server = "smtp.gmail.com"
        try:
            sender_email = os.getenv("sender_email")
            sender_password = os.getenv("sender_password")
        except FileNotFoundError as file_error:
            logger.critical("Failed to fetch auto-mail creds from env: %s", file_error)
            sys.exit()

        try:
            self.send_email(subject, body, to_email, sender_email,
                            sender_password, smtp_server)
            logger.info("mail sent !!")
            if cont_list:
                threading.Thread(
                    target=self.send_mail_trigger_ch_sub_cont, args=(
                                challenge_id, name, description, cont_list
                                )
                    ).start()
                # threading.Timer(
                #     100, self.send_mail_trigger_ch_sub_cont, args=(
                #                 challenge_id, name, description, cont_list
                #                 )
                #     ).start()
            return "mail sent !!"
        except Exception as mail_error:             # pylint: disable=broad-exception-caught
            logger.critical("Mail sending error: %s", mail_error)
            return "Mail sending error: ", mail_error


    def send_mail_trigger_ch_sub_cont(self, challenge_id, name, description, cont_list):
        """mail sender trigger function for challenge submission (contributor mail)"""
        subject = "New Challenge in list !!"
        body = f"""<p>Hello,<br>
                    A new challenge has been created that awaits your solution. Please find the details
                    of the challenge below:<br>
                    <strong>Challenge ID: </strong>{challenge_id}<br>
                    <strong>Challenge Name: </strong>{name}<br>
                    <strong>Challenge Description: </strong>{description}<br>
                    <br></p>
                    <p><small><i>This is a system generated mail and doesn't require any reply or acknowledgement.</i></small></p>"""

        # SMTP server details
        smtp_server = "smtp.gmail.com"
        try:
            sender_email = os.getenv("sender_email")
            sender_password = os.getenv("sender_password")
        except FileNotFoundError as file_error:
            logger.critical("Failed to fetch auto-mail creds from env: %s", file_error)
            sys.exit()

        try:
            for email in cont_list:
                if email and email[0]:
                    self.send_email(subject, body, email[0], sender_email,
                                    sender_password, smtp_server)
                    logger.info("Mail sent to %s !!", email)
        except Exception as mail_error:  # pylint: disable=broad-exception-caught
            logger.critical("Mail sending error: %s", mail_error)


    def subscription_mail_verify(self, to_email, otp):             # pylint: disable=too-many-arguments
        """mail sender trigger function for verifying
           email entered during subscription
        """

        subject = "Welcome Onboard !!"
        body = (
                f"""<p>Hello,<br>
                An account is being created with PetonicAI, and the associated email is yours.
                To verify this action, use this OTP:<br>
                <strong>{otp}</strong><br>
                <br></p>
                <p><small><i>This is a system generated mail and doesn't require any reply or acknowledgement.</i></small></p>"""
            )

        # SMTP server details
        smtp_server = "smtp.gmail.com"
        try:
            sender_email = os.getenv("sender_email")
            sender_password = os.getenv("sender_password")
        except FileNotFoundError as file_error:
            logger.critical("Failed to fetch auto-mail creds from env: %s", file_error)
            sys.exit()

        try:
            self.send_email(subject, body, to_email, sender_email,
                            sender_password, smtp_server)
            logger.info("mail sent !!")
            print ("sent!!")
            return True
        except Exception as mail_error:             # pylint: disable=broad-exception-caught
            logger.critical("Mail sending error: %s", mail_error)
            return False


    def solvai_demo(self, to_email, receiver_name, company_name, details):             # pylint: disable=too-many-arguments
        """mail sender trigger function for solvai demo book functionality
        """

        subject = "SolvAI Demo booked !!"
        body = (
                f"""<p>Hello {receiver_name},<br>
                A demo has been booked for SolvAI feature showcasing. Following are the details for the demo:<br>
                <strong>Attendee</strong>: {receiver_name}<br>
                <strong>Company Name</strong>: {company_name}<br>
                <strong>Details Requested</strong>: {details}
                <p>Some one from the concerned team would get back to you shortly.</p>
                <br></p>
                <p><small><i>This is a system generated mail and doesn't require any reply or acknowledgement.</i></small></p>"""
            )

        # SMTP server details
        smtp_server = "smtp.gmail.com"
        try:
            sender_email = os.getenv("sender_email")
            sender_password = os.getenv("sender_password")
        except FileNotFoundError as file_error:
            logger.critical("Failed to fetch auto-mail creds from env: %s", file_error)
            sys.exit()

        try:
            self.send_email(subject, body, to_email, sender_email,
                            sender_password, smtp_server)
            logger.info("mail sent !!")
            print ("sent!!")
        except Exception as mail_error:             # pylint: disable=broad-exception-caught
            logger.critical("Mail sending error: %s", mail_error)
            return False


    def solvai_support(self, to_email, receiver_name, query):             # pylint: disable=too-many-arguments
        """mail sender trigger function for solvai support ticket book functionality
        """

        subject = "SolvAI support ticket created !!"
        body = (
                f"""<p>Hello {receiver_name},<br>
                A request for support has been raised on SolvAI with following details:<br>
                <strong>Requester</strong>: {receiver_name}<br>
                <strong>Query</strong>: {query}
                <p>Some one from the concerned team would get back to you shortly.</p>
                <br></p>
                <p><small><i>This is a system generated mail and doesn't require any reply or acknowledgement.</i></small></p>"""
            )

        # SMTP server details
        smtp_server = "smtp.gmail.com"
        try:
            sender_email = os.getenv("sender_email")
            sender_password = os.getenv("sender_password")
        except FileNotFoundError as file_error:
            logger.critical("Failed to fetch auto-mail creds from env: %s", file_error)
            sys.exit()

        try:
            self.send_email(subject, body, to_email, sender_email,
                            sender_password, smtp_server)
            logger.info("mail sent !!")
            print ("sent!!")
        except Exception as mail_error:             # pylint: disable=broad-exception-caught
            logger.critical("Mail sending error: %s", mail_error)
            return False


    def support(self, to_email, receiver_first_name, receiver_last_name, service, company, query, table_name,json_data=None):             # pylint: disable=too-many-arguments
        """mail sender trigger function for petonicai / plannex support ticket book functionality
        """
        if table_name == "petonicai_support":
            site = "PetonicAI"
            body = (
                    f"""<p>Hello {receiver_first_name},<br>
                    A request for support has been raised with {site} with following details:<br>
                    <strong>Requester</strong>: {receiver_first_name} {receiver_last_name}<br>
                    <strong>Service</strong>: {service}<br>
                    <strong>Company</strong>: {company}<br>
                    <strong>Query</strong>: {query}
                    <p>Some one from the concerned team would get back to you shortly.</p>
                    <br></p>
                    <p><small><i>This is a system generated mail and doesn't require any reply or acknowledgement.</i></small></p>"""
                )
            subject = f"{site} support ticket created !!"
        elif table_name == "plannex_support":
            site = "Plannex"
            appointment_date = json_data.get('appointment_date', 'N/A')
            appointment_time = json_data.get('appointment_time', 'N/A')
            body = (
                    f"""<p>Hello {receiver_first_name},<br>
                    An appointment has been booked for {site} with following details:<br>
                    <strong>Requester</strong>: {receiver_first_name} {receiver_last_name}<br>
                    <strong>Service</strong>: {service}<br>
                    <strong>Company</strong>: {company}<br>
                    <strong>Query</strong>: {query}<br>
                    <strong>Appointment Date</strong>: {appointment_date}<br>
                    <strong>Appointment Time</strong>: {appointment_time}
                    <p>Some one from the concerned team would get back to you shortly.</p>
                    <br></p>
                    <p><small><i>This is a system generated mail and doesn't require any reply or acknowledgement.</i></small></p>"""
                )
            subject = f"{site} Appointment Booked !!"

        # SMTP server details
        smtp_server = "smtp.gmail.com"
        try:
            sender_email = os.getenv("sender_email")
            sender_password = os.getenv("sender_password")
        except FileNotFoundError as file_error:
            logger.critical("Failed to fetch auto-mail creds from env: %s", file_error)
            sys.exit()

        try:
            self.send_email(subject, body, to_email, sender_email,
                            sender_password, smtp_server)
            logger.info("mail sent !!")
            print ("sent!!")
        except Exception as mail_error:             # pylint: disable=broad-exception-caught
            logger.critical("Mail sending error: %s", mail_error)


    def poc_support(self, to_email, requestor_first_name, requestor_last_name, service, company, query, json_data):             # pylint: disable=too-many-arguments
        """mail sender trigger function for plannex support ticket book functionality to POCs
        """
        site = "Plannex"
        appointment_date = json_data.get('appointment_date', 'N/A')
        appointment_time = json_data.get('appointment_time', 'N/A')
        body = (
                f"""<p>Hello,<br>
                An appointment has been booked for Plannex with following details:<br>
                <strong>Requester</strong>: {requestor_first_name} {requestor_last_name}<br>
                <strong>Service</strong>: {service}<br>
                <strong>Company</strong>: {company}<br>
                <strong>Query</strong>: {query}<br>
                <strong>Appointment Date</strong>: {appointment_date}<br>
                <strong>Appointment Time</strong>: {appointment_time}
                <p>Some one from the concerned team would get back to you shortly.</p>
                <br></p>
                <p><small><i>This is a system generated mail and doesn't require any reply or acknowledgement.</i></small></p>"""
            )
        subject = f"Plannex Appointment Booked !!"

        # SMTP server details
        smtp_server = "smtp.gmail.com"
        try:
            sender_email = os.getenv("sender_email")
            sender_password = os.getenv("sender_password")
        except FileNotFoundError as file_error:
            logger.critical("Failed to fetch auto-mail creds from env: %s", file_error)
            sys.exit()

        try:
            self.send_email(subject, body, to_email, sender_email,
                            sender_password, smtp_server)
            logger.info("mail sent !!")
            print ("sent!!")
        except Exception as mail_error:             # pylint: disable=broad-exception-caught
            logger.critical("Mail sending error: %s", mail_error)
