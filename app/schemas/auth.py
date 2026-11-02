from datetime import datetime
from typing import TypedDict
from schemas.doctor import DoctorRead
from schemas.nurse import NurseRead
from schemas.shared.base_schema import BaseSchema
from schemas.shared.types import PasswordStr, PhoneStr
from schemas.user import UserRead


class AccessTokenPayload(TypedDict):
    user_id: int
    user_role: str


class EncodedAccessTokenPayload(AccessTokenPayload):
    exp: datetime
    iat: datetime


class AccessToken(BaseSchema):
    access_token: str
    token_type: str


class AuthPayload(BaseSchema):
    phone: PhoneStr
    password: PasswordStr


class AuthResponse(BaseSchema):
    user: UserRead
    profile: DoctorRead | NurseRead
    token: AccessToken
