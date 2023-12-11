"""
This module defines Pydantic models to enforce validation
rules for email addresses, passwords, user roles, etc.
These models provide a structured and validated way to
handle incoming JSON payloads in FastAPI routes.
"""
from typing import Any
# from pydantic import BaseModel, EmailStr, constr, Union, PositiveInt, ValidationError, validator
from pydantic import BaseModel, EmailStr, constr, PositiveInt


class LoginRequest(BaseModel):
    """Pydantic model for the login request payload.

    Attributes:
        email (EmailStr): The user's email address.
        password (str): The user's password.
        role (str): The user's role, should be one of "initiator", "contributor", or "stakeholder".
    """
    email: EmailStr
    password: str
    role: constr(pattern="^(initiator|contributor|stakeholder)$")


class SignupRequest(BaseModel):
    """Pydantic model for the signup request payload.

    Attributes:
        email (EmailStr): The user's email address.
        role (str): The user's role, should be one of "initiator", "contributor", or "stakeholder".
        f_name (str): The user's first name.
        l_name (str): The user's last name.
        company_id (Union[str, int]): The user's company ID, can be either a string or an integer.
    """
    email: EmailStr
    role: constr(pattern="^(initiator|contributor|stakeholder)$")
    f_name: str
    l_name: str
    # company_id: Union[str, int]
    company_id: Any


class ValidationRequest(BaseModel):
    """Pydantic model for a validation request payload.

    Attributes:
        email (EmailStr): The user's email address.
        role (str): The user's role, should be one of "initiator", "contributor", or "stakeholder".
    """
    email: EmailStr
    role: constr(pattern="^(initiator|contributor|stakeholder)$")


class ForgotPasswordRequest(BaseModel):
    """Pydantic model for a Forgot Password request payload.

    Attributes:
        email (EmailStr): The user's email address.
        role (str): The user's role, should be one of "initiator", "contributor", or "stakeholder".
    """
    email: EmailStr
    role: constr(pattern="^(initiator|contributor|stakeholder)$")


class ChangePasswordRequest(BaseModel):
    """Pydantic model for the change-password request payload.

    Attributes:
        email (EmailStr): The user's email address.
        role (str): The user's role, should be one of "initiator", "contributor", or "stakeholder".
        current_password (str): The user's current password.
        new_password (str): The new password to set.
    """
    email: EmailStr
    role: constr(pattern="^(initiator|contributor|stakeholder)$")
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


class ChallengeJsonDataFetchRequest(BaseModel):
    """Pydantic model for the challenge-json-data-fetch request payload.

    Attributes:
        challenge_identifier (Any): The identifier of the challenge, which can be any type.
    """
    challenge_identifier: Any


class ChallengeCreationRequest(BaseModel):
    """Pydantic model for the challenge-creation request payload.

    Attributes:
        challenge_id (PositiveInt): The ID of the challenge.
        initiator_id (str): The initiator ID, a combination of role and email.
        date (str): The date of the challenge in the format 'YYYY-MM-DD'.
        industry (str): The industry associated with the challenge.
        process (str): The process associated with the challenge.
        domain (str): The domain associated with the challenge.
        background (str): The background information for the challenge.
    """
    challenge_id: PositiveInt
    initiator_id: constr(
        pattern=r'^(initiator|stakeholder|contributor)_[\w.-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$'
        )
    date: constr(pattern=r'\d{4}-\d{2}-\d{2}')
    industry: str
    process: str
    domain: str
    background: str


# class ChallengeCountRequest(BaseModel):
#     initiator_id: constr(pattern=r'^[\w.-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$')

#     @validator("initiator_id")
#     def validate_initiator_id(cls, value):
#         parts = value.split("_", 1)
#         if len(parts) != 2:
#             raise ValidationError("Invalid initiator_id format")

#         role, email = parts
#         if role not in ["initiator", "stakeholder", "contributor"]:
#             raise ValidationError("Invalid role")
#         return value


class ChallengeCountRequest(BaseModel):
    """Pydantic model for the challenge-count request payload.

    Attributes:
        initiator_id (str): The initiator ID, a combination of role and email.
    """
    initiator_id: constr(
        pattern=r'^(initiator|stakeholder|contributor)_[\w.-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$'
        )
