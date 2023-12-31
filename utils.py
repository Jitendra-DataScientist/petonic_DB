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


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

# Create a logger instance
logger = logging.getLogger(__name__)


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

        except Exception as mail_error:             # pylint: disable=broad-exception-caught
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
        except Exception as mail_error1:             # pylint: disable=broad-exception-caught
            logger.critical("Failed to fetch auto-mail creds from env: %s", mail_error1)
            sender_email = "automail.petonic@gmail.com"
            sender_password = "efvumbcfgryjachh"

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

        except Exception as mail_error:             # pylint: disable=broad-exception-caught
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
        except Exception as mail_error1:             # pylint: disable=broad-exception-caught
            logger.critical("Failed to fetch auto-mail creds from env: %s", mail_error1)
            sys.exit()

        try:
            self.send_email(subject, body, to_email, sender_email,
                            sender_password, smtp_server)
            logger.info("mail sent !!")
            return "mail sent !!"
        except Exception as mail_error2:             # pylint: disable=broad-exception-caught
            logger.critical("Mail sending error: %s", mail_error2)
            return "Mail sending error: ", mail_error2
