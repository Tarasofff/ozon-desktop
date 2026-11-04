from schemas.doctor import DoctorRead
from schemas.nurse import NurseRead
from schemas.shared import BaseCreate, BaseSchema
from schemas.shared.types import PasswordStr, PhoneStr
from schemas.user import UserRead


class AccessToken(BaseSchema):
    access_token: str
    token_type: str


class AuthPayload(BaseCreate):
    phone: PhoneStr
    password: PasswordStr


class AuthResponse(BaseSchema):
    user: UserRead
    profile: DoctorRead | NurseRead
    token: AccessToken
