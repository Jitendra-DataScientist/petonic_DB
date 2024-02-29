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

        subject = "Innovation.ai SignUp"
        try:
            logo_url = os.getenv("logo_url")
            body = (
                    f"""<p>Hello,<br>
                    An account with <strong>{role}</strong> role has been created on Innovation.ai,
                    the user ID for which is your mail ID and password for which is <strong>
                    {first_password}</strong>.<br> Please log in using these credentials.</p>
                    <p>If you do not recognise this activity, please ignore this email.</p>
                    <p>Best regards,<br>
                    Petonic Team</p>
                    <img src={logo_url} alt="Petonic Company Logo">"""
                )

        except FileNotFoundError as file_error:
            logger.critical("Failed to load logo_url from .env: %s", file_error)
            body = (
                    f"""<p>Hello,<br>
                    An account with <strong>{role}</strong> role has been created on Innovation.ai,
                    the user ID for which is your mail ID and password for which is <strong>
                    {first_password}</strong>.<br> Please log in using these credentials.</p>
                    <p>If you do not recognise this activity, please ignore this email.</p>
                    <p>Best regards,<br>
                    Petonic Team</p>"""
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

        except FileNotFoundError as file_error:
            logger.critical("Failed to load logo_url from .env: %s", file_error)
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
        try:
            logo_url = os.getenv("logo_url")
            body = (
                    f"""<p>Hello,<br>
                    Your password has been changed to <strong>{new_password}
                    </strong> successfully.<br>
                    Please log in using this password now.
                    If you do not recognize this activity, contact your admin.
                    </p>
                    <p>Best regards,<br>
                    Petonic Team</p>
                    <img src={logo_url} alt="Petonic Company Logo">"""
                )

        except FileNotFoundError as file_error:
            logger.critical("Failed to load logo_url from .env: %s", file_error)
            body = (
                    f"""<p>Hello,<br>
                    Your password has been changed to <strong>{new_password}
                    </strong> successfully.<br>
                    Please log in using this password now.
                    If you do not recognize this activity, contact your admin.
                    </p>
                    <p>Best regards,<br>
                    Petonic Team</p>"""
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
        try:
            logo_url = os.getenv("logo_url")
            body = (
                    f"""<p>Hello,<br>
                    Your role for Innovation.ai has now been set to <strong>{role}</strong>.<br></p>
                    <p>Best regards,<br>
                    Petonic Team</p>
                    <img src={logo_url} alt="Petonic Company Logo">"""
                )

        except FileNotFoundError as file_error:
            logger.critical("Failed to load logo_url from .env: %s", file_error)
            body = (
                    f"""<p>Hello,<br>
                    Your role for Innovation.ai has now been set to <strong>{role}</strong>.<br></p>
                    <p>Best regards,<br>
                    Petonic Team</p>"""
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
            try:
                logo_url = os.getenv("logo_url")
                body = (
                        f"""<p>Hello,<br>
                        Your account for Innovation.ai has now been activated.<br></p>
                        <p>Best regards,<br>
                        Petonic Team</p>
                        <img src={logo_url} alt="Petonic Company Logo">"""
                    )

            except FileNotFoundError as file_error:
                logger.critical("Failed to load logo_url from .env: %s", file_error)
                body = (
                        """<p>Hello,<br>
                        Your account for Innovation.ai has now been activated.<br></p>
                        <p>Best regards,<br>
                        Petonic Team</p>"""
                    )
        else:
            subject = "Account Deactivated"
            try:
                logo_url = os.getenv("logo_url")
                body = (
                        f"""<p>Hello,<br>
                        Your account for Innovation.ai has now been deactivated.<br></p>
                        <p>Best regards,<br>
                        Petonic Team</p>
                        <img src={logo_url} alt="Petonic Company Logo">"""
                    )

            except FileNotFoundError as file_error:
                logger.critical("Failed to load logo_url from .env: %s", file_error)
                body = (
                        """<p>Hello,<br>
                        Your account for Innovation.ai has now been deactivated.<br></p>
                        <p>Best regards,<br>
                        Petonic Team</p>"""
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
        """mail sender trigger function"""

        subject = "Challenge Initiated !!"
        try:
            logo_url = os.getenv("logo_url")
            body = (
                    f"""<p>Hello,<br>
                    You have successfully initiated a challenge. Please find the details
                    of challenge below:<br>
                    <strong>challenge_id: </strong>{challenge_id}
                    <strong>industry: </strong>{industry}
                    <strong>domain: </strong>{domain}
                    <strong>process: </strong>{process}
                    <br></p>
                    <p>Best regards,<br>
                    Petonic Team</p>
                    <img src={logo_url} alt="Petonic Company Logo">"""
                )

        except FileNotFoundError as file_error:
            logger.critical("Failed to load logo_url from .env: %s", file_error)
            body = (
                    f"""<p>Hello,<br>
                    You have successfully initiated a challenge. Please find the details
                    of challenge below:<br>
                    <strong>challenge_id: </strong>{challenge_id}<br>
                    <strong>industry: </strong>{industry}<br>
                    <strong>domain: </strong>{domain}<br>
                    <strong>process: </strong>{process}<br>
                    <br></p>
                    <p>Best regards,<br>
                    Petonic Team</p>"""
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
