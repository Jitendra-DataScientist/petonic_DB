"""
This module defines Pydantic models to enforce validation
rules for email addresses, passwords, user roles, etc.
These models provide a structured and validated way to
handle incoming JSON payloads in FastAPI routes.
"""
from typing import Dict, Union, Any
# from pydantic import BaseModel, EmailStr, constr, Union, PositiveInt, ValidationError, validator
from pydantic import BaseModel, EmailStr, constr, PositiveInt


class LoginRequest(BaseModel):
    """Pydantic model for the login request payload.

    Attributes:
        email (EmailStr): The user's email address.
        password (str): The user's password.
        # role (str): The user's role, should be one of "initiator", "contributor", or "approver".
    """
    email: EmailStr
    password: str
    # role: constr(pattern="^(initiator|contributor|approver)$")


class SignupRequest(BaseModel):
    """Pydantic model for the signup request payload.

    Attributes:
        email (EmailStr): The user's email address.
        role (str): The user's role, should be one of "initiator", "contributor", or "approver".
        f_name (str): The user's first name.
        l_name (str): The user's last name.
        employee_id (Union[str, int]): The user's employee ID, can be either a string
                                       or an integer, or a combination of both.
    """
    email: EmailStr
    role: constr(pattern="^(initiator|contributor|approver)$")
    f_name: str
    l_name: str
    # company_id: Union[str, int]
    employee_id: Any


class ResendSignupMailRequest(BaseModel):
    """Pydantic model for the resend signup mail request payload.

    Attributes:
        email (EmailStr): The user's email address.
        # role (str): The user's role, should be one of "initiator", "contributor", or "approver".
    """
    email: EmailStr
    # role: constr(pattern="^(initiator|contributor|approver)$")


class ValidationRequest(BaseModel):
    """Pydantic model for a validation request payload.

    Attributes:
        email (EmailStr): The user's email address.
        # role (str): The user's role, should be one of "initiator", "contributor", or "approver".
    """
    email: EmailStr
    # role: constr(pattern="^(initiator|contributor|approver)$")


class ForgotPasswordRequest(BaseModel):
    """Pydantic model for a Forgot Password request payload.

    Attributes:
        email (EmailStr): The user's email address.
        # role (str): The user's role, should be one of "initiator", "contributor", or "approver".
    """
    email: EmailStr
    # role: constr(pattern="^(initiator|contributor|approver)$")


class ChangePasswordRequest(BaseModel):
    """Pydantic model for the change-password request payload.

    Attributes:
        email (EmailStr): The user's email address.
        # role (str): The user's role, should be one of "initiator", "contributor", or "approver".
        current_password (str): The user's current password.
        new_password (str): The new password to set.
    """
    email: EmailStr
    # role: constr(pattern="^(initiator|contributor|approver)$")
    current_password: str
    new_password: str


class DomainDropdownRequest(BaseModel):
    """Pydantic model for the domain-dropdown request payload.

    Attributes:
        industry_id (int): The ID of the industry.
    """
    industry_id: PositiveInt


class ProcessDropdownRequest(BaseModel):
    """Pydantic model for the process-dropdown request payload.

    Attributes:
        domain_id (int): The ID of the domain.
    """
    domain_id: PositiveInt


class UpdateChallengeStatusRequest(BaseModel):
    """Pydantic model for the update-challenge-status request payload.

    Attributes:
        challenge_id (int): The ID of the challenge to update.
        challenge_status (str): The new status for the challenge.
    """
    challenge_id: PositiveInt
    challenge_status: constr(max_length=10)


class FetchChallengeStatusRequest(BaseModel):
    """Pydantic model for the fetch-challenge-status request payload.

    Attributes:
        challenge_id (int): The ID of the challenge to fetch the status for.
    """
    challenge_id: PositiveInt


class ChallengeJsonDataWriteRequest(BaseModel):
    """Pydantic model for the challenge-json-data-write request payload.

    Attributes:
        challenge_id (PositiveInt): The id of the challenge, which should be a positive integer.
        json_data (python dictionary): the python dict can have keys that numbers, strings or
                                       combination of both, the values could be of any type.
    """
    challenge_id: PositiveInt
    json_data: Dict[Union[str, int], Any]


class ChallengeJsonDataFetchRequest(BaseModel):
    """Pydantic model for the challenge-json-data-fetch request payload.

    Attributes:
        challenge_id (PositiveInt): The id of the challenge, which should be a positive integer.
    """
    challenge_id: PositiveInt


class ChallengeInitiationRequest(BaseModel):
    """Pydantic model for the challenge-creation request payload.

    Attributes:
        # initiator_id (str): The initiator ID, a combination of role and email.
        initiator_id (str): The email ID of initiator.
        initiation_timestamp (str): The initiation date of the challenge in the format 'YYYY-MM-DD'.
        industry (str): The industry associated with the challenge.
        process (str): The process associated with the challenge.
        domain (str): The domain associated with the challenge.
    """
    # initiator_id: constr(
    #     pattern=r'^(initiator|approver|contributor)_[\w.-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$'
    #     )
    initiator_id: EmailStr
    initiation_timestamp: constr(pattern=r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    industry: str
    process: str
    domain: str


# class ChallengeCountRequest(BaseModel):
#     initiator_id: constr(pattern=r'^[\w.-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$')

#     @validator("initiator_id")
#     def validate_initiator_id(cls, value):
#         parts = value.split("_", 1)
#         if len(parts) != 2:
#             raise ValidationError("Invalid initiator_id format")

#         role, email = parts
#         if role not in ["initiator", "approver", "contributor"]:
#             raise ValidationError("Invalid role")
#         return value


class ChallengeCountRequest(BaseModel):
    """Pydantic model for the challenge-count request payload.

    Attributes:
        # initiator_id (str): The initiator ID, a combination of role and email.
        initiator_id (str): The email ID of initiator.
    """
    # initiator_id: constr(
    #     pattern=r'^(initiator|approver|contributor)_[\w.-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$'
    #     )
    initiator_id: EmailStr


class ChallengeCreationRequest(BaseModel):
    """Pydantic model for the challenge-creation request payload.

    Attributes:
        challenge_id (PositiveInt): The ID of the challenge.
        creation_timestamp (str): The initiator ID, a combination of role and email.
        name (str): Name of the challenge.
        description (str): Description of the challenge.
    """
    challenge_id: PositiveInt
    creation_timestamp: constr(pattern=r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    name: str
    description: str


class ViewListRequest(BaseModel):
    """Pydantic model for the view-list request payload.
       Note this is only for the post request.

    Attributes:
        # initiator_id (str): initiator_id, for eg., initiator_johndoe@example.com
        initiator_id (str): The email ID of initiator.
    """
    # initiator_id: constr(
    #     pattern=r'^(initiator|approver|contributor)_[\w.-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$'
    #     )
    initiator_id: EmailStr


class FlipUserStatusRequest(BaseModel):
    """Pydantic model for the flip_user_status
       request payload.
       Note this is only for the post request.

    Attributes:
        email (str): The email ID of user.
    """
    email: EmailStr


class EditUserDetailsRequest(BaseModel):
    """Pydantic model for the edit user details request payload.

    Attributes:
        email (EmailStr): The user's email address (mandatory).
        f_name (str): The user's first name.
        l_name (str): The user's last name.
        role (str): The user's role.
        employee_id (PositiveInt): The user's employee ID.
    """
    email: EmailStr
    f_name: str = None
    l_name: str = None
    role: str = None
    employee_id: PositiveInt = None
