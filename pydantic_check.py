"""
This module defines Pydantic models to enforce validation
rules for email addresses, passwords, user roles, etc.
These models provide a structured and validated way to
handle incoming JSON payloads in FastAPI routes.
"""
from typing import Dict, Union, Any, Optional, List
from pydantic import BaseModel, EmailStr, constr, PositiveInt
# from pydantic import Union, ValidationError, validator


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

    # @classmethod
    # @validator("email", pre=True)
    # def convert_to_lower(self, value):
    #     """Validator to convert email to lowercase."""
    #     return value.lower()


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
    admin_email: EmailStr = None
    admin_password: str = None
    subscription_id: str

    # @classmethod
    # @validator("email", "admin_email", pre=True)
    # def convert_to_lower(self, value):
    #     """Validator to convert admin_email and email to lowercase."""
    #     return value.lower() if value else value


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
    admin_email: EmailStr
    admin_password: str

    # @classmethod
    # @validator("email", "admin_email", pre=True)
    # def convert_to_lower(self, value):
    #     """Validator to convert admin_email and email to lowercase."""
    #     return value.lower()


class ValidationRequest(BaseModel):
    """Pydantic model for a validation request payload.

    Attributes:
        email (EmailStr): The user's email address.
        # role (str): The user's role, should be one of "initiator", "contributor", or "approver".
    """
    email: EmailStr
    # role: constr(pattern="^(initiator|contributor|approver)$")

    # @classmethod
    # @validator("email", pre=True)
    # def convert_to_lower(self, value):
    #     """Validator to convert email to lowercase."""
    #     return value.lower()


class ForgotPasswordRequest(BaseModel):
    """Pydantic model for a Forgot Password request payload.

    Attributes:
        email (EmailStr): The user's email address.
        # role (str): The user's role, should be one of "initiator", "contributor", or "approver".
    """
    email: EmailStr
    # role: constr(pattern="^(initiator|contributor|approver)$")

    # @classmethod
    # @validator("email", pre=True)
    # def convert_to_lower(self, value):
    #     """Validator to convert email to lowercase."""
    #     return value.lower()


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

    # @classmethod
    # @validator("email", pre=True)
    # def convert_to_lower(self, value):
    #     """Validator to convert email to lowercase."""
    #     return value.lower()


# class DomainDropdownRequest(BaseModel):
#     """Pydantic model for the domain-dropdown request payload.

#     Attributes:
#         industry_id (int): The ID of the industry.
#     """
#     industry_id: PositiveInt


# class ProcessDropdownRequest(BaseModel):
#     """Pydantic model for the process-dropdown request payload.

#     Attributes:
#         domain_id (int): The ID of the domain.
#     """
#     domain_id: PositiveInt


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

    # @classmethod
    # @validator("initiator_id", pre=True)
    # def convert_to_lower(self, value):
    #     """Validator to convert initiator_id to lowercase."""
    #     return value.lower()


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

    # @classmethod
    # @validator("initiator_id", pre=True)
    # def convert_to_lower(self, value):
    #     """Validator to convert initiator_id to lowercase."""
    #     return value.lower()


class ChallengeCreationRequest(BaseModel):
    """Pydantic model for the challenge-creation request payload.

    Attributes:
        challenge_id (str): The ID of the challenge.
        creation_timestamp (str): The initiator ID, a combination of role and email.
        name (str): Name of the challenge.
        description (str): Description of the challenge.
    """
    challenge_id: str
    creation_timestamp: Optional[constr(pattern=r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')] = None
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
        contributor: Optional[bool] = None
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
    contributor: Optional[bool] = None
    subscription_id: str

    # @classmethod
    # @validator("initiator_id", "approver_id", pre=True)
    # def convert_to_lower_case(self, value):
    #     """Validator to convert initiator_id and approver_id to lowercase."""
    #     if value is not None:
    #         if isinstance(value, list):
    #             ret = [email.lower() for email in value]
    #         elif isinstance(value, str):
    #             ret = value.lower()
    #     else: ret = value
    #     return ret


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

    # @classmethod
    # @validator("email", "admin_email", pre=True)
    # def convert_to_lower(self, value):
    #     """Validator to convert email and admin_email to lowercase."""
    #     return value.lower() if value else value


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
    employee_id: Any = None
    admin_email: EmailStr
    admin_password: str

    # @classmethod
    # @validator("email", "admin_email", pre=True)
    # def convert_to_lower(self, value):
    #     """Validator to convert email and admin_email to lowercase."""
    #     return value.lower()


class AdminViewListRequest(BaseModel):
    """Pydantic model for the admin-view-list request
    """
    subscription_id: str


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

    # @classmethod
    # @validator('approver_id', pre=True)
    # def validate_approver_id(self, value):
    #     """Validator to ensure approver_id is always in lowercase."""
    #     return value.lower()


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

    # @classmethod
    # @validator('approver_id', pre=True)
    # def validate_approver_id(self, value):
    #     """Validator to ensure approver_id is always in lowercase."""
    #     return value.lower()


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

    # @classmethod
    # @validator('contributor_id', pre=True)
    # def convert_to_lower(self, value):
    #     """Validator to convert contributor_id to lowercase."""
    #     return value.lower()


class GetUserDetailsRequest(BaseModel):
    """Pydantic model for get-user-details request payload.

    Attributes:
        user_ids (List[EmailStr]): The list of IDs whose details are to be fetched.
    """
    user_ids: List[EmailStr]

    # @classmethod
    # @validator('user_ids', each_item=True, pre=True)
    # def convert_to_lowercase(self, value):
    #     """Validator to convert user_ids to lowercase."""
    #     return value.lower()


class ProjectInitiateRequest(BaseModel):
    """Pydantic model for project-initiate request payload.

    Attributes:
        challenge_id (str): The id of the challenge, which should be a positive integer.
        pm_id (EmailStr): The project manager's email address.
        pm_tool (str): The project management tool being used.
    """
    challenge_id: str
    pm_id: EmailStr
    pm_tool: str

    # @classmethod
    # @validator('pm_id', pre=True)
    # def validate_pm_id(self, value):
    #     """Validator to convert pm_id to lowercase."""
    #     return value.lower()


class GenAPIAnalytics(BaseModel):
    """Pydantic model for gen-ai-api analytics request payload.

    Attributes:
        challenge_id (str): The id of the challenge, which should be a positive integer.
        gen_ai_api (str): The name of the GenAI API (probably, the part after the route).
        input (Dict): The input parameters for the API.
        prompt (str): The prompt used to generate response from the model.
        output (Dict): The response from the API.
        modelParams (Dict): The parameters/configurations of the model used.
        tokens (int): The number of tokens used in a particular API call.
        cost (str): The total cost incurred in the API call (this is passed as string and
                    converted into decimal before passing to DB).
        # timestamp (float): The timestamp at which the logs came.
    """
    gen_ai_api: str
    challenge_id: str
    input: Dict
    prompt: str
    output: str
    modelParams: str
    tokens: int
    cost: str
    # timestamp: float


# class GenAITokenCost(BaseModel):
#     """Pydantic model for gen-ai-token-cost request payload.

#     Attributes:
#         challenge_id (str): The id of the challenge, which should be a positive integer.
#     """
#     challenge_id: str


class GenAITokenCostUserWise(BaseModel):
    """Pydantic model for gen-ai-token-cost request payload.

    Attributes:
        start_epoch (float): The data after this timestamp needs to be fetched.
        end_epoch (float): The data before this timestamp needs to be fetched.
    """
    start_epoch: float
    end_epoch: float


class FirstAdd(BaseModel):
    """Pydantic model for firstAdd request payload."""
    email: EmailStr
    f_name: str
    l_name: str
    # company_id: Union[str, int]
    employee_id: Any
    plan: str
    users_count: int
    company_name: str
    phone: str
    country: str
    address_line1: str = None
    address_line2: str = None


class VerifyOTP(BaseModel):
    """Pydantic model for verify-otp request payload."""
    subscription_id: str
    otp: str


class ResendOTP(BaseModel):
    """Pydantic model for resend-otp request payload."""
    subscription_id: str
    email: EmailStr


class EmailModify(BaseModel):
    """Pydantic model for resend-otp request payload."""
    subscription_id: str
    new_email: EmailStr


class SecondAdd(BaseModel):
    """Pydantic model for second-add request payload."""
    subscription_id: str
    payment_mode: str
    amount: str
    payment_status: str


class FirstUser(BaseModel):
    """Pydantic model for first-user request payload."""
    email: EmailStr


class FlipFirstUserStatus(BaseModel):
    """Pydantic model for flip-first-user-status request payload."""
    email: EmailStr


class LeaderboardBestProject(BaseModel):
    """Pydantic model for leaderboard/best-project request payload."""
    subscription_id: str


class SolvaiSupport(BaseModel):
    """Pydantic model for solvai-support request payload."""
    subscription_id: str
    email: EmailStr
    name: str
    # phone: Optional[str] = None
    query: str


class PetonicaiSupport(BaseModel):
    """Pydantic model for petonicai-support request payload."""
    email: EmailStr
    last_name: str
    first_name: str
    service: str
    company: str
    phone: Optional[str] = None
    query: str
    json_data: Optional[Dict] = None


class SolvaiDemo(BaseModel):
    """Pydantic model for solvai-demo request payload."""
    email: EmailStr
    name: str
    company_name: str
    details: str


class PlannexContactUs(BaseModel):
    """Pydantic model for plannex-contact-us request payload."""
    email: EmailStr
    last_name: str
    first_name: str
    company: str
    query: str
    json_data: Optional[Dict] = None


class PlannexLogin(BaseModel):
    """Pydantic model for plannex-login request payload."""
    email: EmailStr
    password: str
