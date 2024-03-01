"""
This module defines Pydantic models to enforce validation
rules for email addresses, passwords, user roles, etc.
These models provide a structured and validated way to
handle incoming JSON payloads in FastAPI routes.
"""
from typing import Dict, Union, Any, Optional, List
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
        admin_email (EmailStr): The email of admin account.
        admin_password (str): The password of admin account.
    """
    email: EmailStr
    role: constr(pattern="^(initiator|contributor|approver|admin|pm)$")
    f_name: str
    l_name: str
    # company_id: Union[str, int]
    employee_id: Any
    admin_email: EmailStr
    admin_password: str


class ResendSignupMailRequest(BaseModel):
    """Pydantic model for the resend signup mail request payload.

    Attributes:
        email (EmailStr): The user's email address.
        role (str): The user's role, should be one of "initiator", "contributor", or "approver".
        admin_email (EmailStr): The email of admin account.
        admin_password (str): The password of admin account.
    """
    email: EmailStr
    role: constr(pattern="^(initiator|contributor|approver|pm)$")
    admin_email: EmailStr = None
    admin_password: str = None


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
        challenge_id (str): The ID of the challenge to update.
        challenge_status (str): The new status for the challenge.
    """
    challenge_id: str
    challenge_status: constr(max_length=10)


class FetchChallengeStatusRequest(BaseModel):
    """Pydantic model for the fetch-challenge-status request payload.

    Attributes:
        challenge_id (str): The ID of the challenge to fetch the status for.
    """
    challenge_id: str


class ChallengeJsonDataWriteRequest(BaseModel):
    """Pydantic model for the challenge-json-data-update request payload.

    Attributes:
        challenge_id (str): The id of the challenge, which should be a positive integer.
        json_data (python dictionary): the python dict can have keys that numbers, strings or
                                       combination of both, the values could be of any type.
    """
    challenge_id: str
    json_data: Dict[Union[str, int], Any]


class ChallengeJsonDataFetchRequest(BaseModel):
    """Pydantic model for the challenge-json-data-fetch request payload.

    Attributes:
        challenge_id (str): The id of the challenge, which should be a positive integer.
    """
    challenge_id: str


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
        challenge_id (str): The ID of the challenge.
        creation_timestamp (str): The initiator ID, a combination of role and email.
        name (str): Name of the challenge.
        description (str): Description of the challenge.
    """
    challenge_id: str
    creation_timestamp: constr(pattern=r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    name: str
    description: str


class ViewListRequest(BaseModel):
    """Pydantic model for the view-list request payload.
       Note this is only for the post request.

    Attributes:
        # initiator_id (str): initiator_id, for eg., initiator_johndoe@example.com
        initiator_id Optional[List[EmailStr]]: The email ID of initiator (optional).
        initiation_start_date (Optional[str]): The initiation start date (optional).
        initiation_end_date (Optional[str]): The initiation end date (optional).
        creation_start_date (Optional[str]): The creation start date (optional).
        creation_end_date (Optional[str]): The creation end date (optional).
        creation_date_null: Optional[bool] = whether to include the challenges that are under draft,
                                                i.e, creation_date is null (optional).
        lower_index (Optional[int]): The lower index (optional).
        upper_index (Optional[int]): The upper index (optional).
        status: Optional[List[str]] = status of the challenges being fetched (optional).
        industry: Optional[List[str]] = related industry of challenge
        domain: Optional[List[str]] = related domain of challenge
        process: Optional[List[str]] = related process of challenge
        approver_id: Optional[List[EmailStr]] = The email ID of approver (optional).
    """
    # initiator_id: constr(
    #     pattern=r'^(initiator|approver|contributor)_[\w.-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$'
    #     )
    initiator_id: Optional[List[EmailStr]] = None
    initiation_start_date: Optional[str] = None
    initiation_end_date: Optional[str] = None
    creation_start_date: Optional[str] = None
    creation_end_date: Optional[str] = None
    creation_date_null: Optional[bool] = None
    lower_index: Optional[int] = None
    upper_index: Optional[int] = None
    status: Optional[List[str]] = None
    industry: Optional[List[str]] = None
    domain: Optional[List[str]] = None
    process: Optional[List[str]] = None
    approver_id: Optional[List[EmailStr]] = None


class FlipUserStatusRequest(BaseModel):
    """Pydantic model for the flip_user_status
       request payload.
       Note this is only for the post request.

    Attributes:
        email (EmailStr): The email ID of user.
        admin_email (EmailStr): The email of admin account.
        admin_password (str): The password of admin account.
    """
    email: EmailStr
    admin_email: EmailStr
    admin_password: str


class EditUserDetailsRequest(BaseModel):
    """Pydantic model for the edit user details request payload.

    Attributes:
        email (EmailStr): The user's email address (mandatory).
        f_name (str): The user's first name.
        l_name (str): The user's last name.
        role (str): The user's role.
        employee_id (PositiveInt): The user's employee ID.
        admin_email (EmailStr): The email of admin account.
        admin_password (str): The password of admin account.
    """
    email: EmailStr
    f_name: str = None
    l_name: str = None
    role: str = None
    employee_id: PositiveInt = None
    admin_email: EmailStr
    admin_password: str


class SettinParamaterKeyParametersRequest(BaseModel):
    """Pydantic model for the setting-parameter-key-parameters request payload.

    Attributes:
        industry (str): The industry associated with the challenge.
        process (str): The process associated with the challenge.
        domain (str): The domain associated with the challenge.
    """
    industry: str
    process: str
    domain: str


class ContributorApproverJsonDataWriteRequest(BaseModel):
    """Pydantic model for the contributor-approver-json-data-update request payload.

    Attributes:
        challenge_id (str): The id of the challenge, which should be a positive integer.
        json_data (python dictionary): the python dict can have keys that numbers, strings or
                                       combination of both, the values could be of any type.
    """
    challenge_id: str
    json_data: Dict[Union[str, int], Any]


class ContributorApproverJsonDataFetchRequest(BaseModel):
    """Pydantic model for the contributor-approver-json-data-fetch request payload.

    Attributes:
        challenge_id (str): The id of the challenge, which should be a positive integer.
    """
    challenge_id: str


# class AddContributorRequest(BaseModel):
#     """Pydantic model for add-contributor request payload.

#     Attributes:
#         contributor_id (EmailStr): The contributor's email address.
#         challenge_id (PositiveInt): The id of the challenge, which should be a positive integer.
#     """
#     contributor_id: EmailStr
#     challenge_id: PositiveInt


class AddApproverRequest(BaseModel):
    """Pydantic model for add-approver request payload.

    Attributes:
        approver_id (EmailStr): The approver's email address.
        challenge_id (str): The id of the challenge, which should be a positive integer.
    """
    approver_id: EmailStr
    challenge_id: str


class AddApproverCommentRequest(BaseModel):
    """Pydantic model for add-approver request payload.

    Attributes:
        approver_id (EmailStr): The approver's email address.
        challenge_id (str): The id of the challenge, which should be a positive integer.
        approver_comment (str): The corresponding comment of the approver
    """
    approver_id: EmailStr
    challenge_id: str
    approver_comment: str


class ViewFileListRequest(BaseModel):
    """Pydantic model for view-file-list request payload.

    Attributes:
        path_key_prefix (str): The corresponding comment of the approver
    """
    path_key_prefix: str


class ContributorSolutionUploadRequest(BaseModel):
    """Pydantic model for contributor-solution request payload.

    Attributes:
        challenge_id (str): The id of the challenge, which should be a positive integer.
        contributor_id (EmailStr): The contributor's email address.
        solution_json (Dict): The contributor's solution.
    """
    challenge_id: str
    contributor_id: EmailStr
    solution_json: Dict[Union[str, int], Any]


class GetUserDetailsRequest(BaseModel):
    """Pydantic model for get-user-details request payload.

    Attributes:
        user_ids: List[EmailStr]: The list of IDs whose details are to be fetched.
    """
    user_ids: List[EmailStr]


class ProjectInitiateRequest(BaseModel):
    """Pydantic model for project-initiate request payload.

    Attributes:
        challenge_id (str): The id of the challenge, which should be a positive integer.
        pm_id: EmailStr: The project manager's email address.
        pm_tool: str: The project management tool being used.
    """
    challenge_id: str
    pm_id: EmailStr
    pm_tool: str
