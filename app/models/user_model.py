from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import date

from models.timestamp_model import Timestamp


class UserEntity(Timestamp):
    id: int


class UserModel(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    phone: str
    email: Optional[EmailStr]
    date_of_birth: date
    password: str
    is_active: bool
    role_id: int


class UserLoginRequestSchema(BaseModel):
    phone: str
    password: str


class UserLoginResponseSchema(UserEntity):
    first_name: str
    middle_name: str
    last_name: str
    phone: str
    email: EmailStr
    date_of_birth: date
    is_active: bool
    role_id: int
    token: str
    token_type: str


class UserPartialSchema(BaseModel):
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    phone: Optional[str]
    email: Optional[EmailStr]
    date_of_birth: Optional[date]
    password: Optional[str]
    role_id: Optional[int]
    is_active: Optional[bool]
