from typing import Optional
from pydantic import BaseModel, EmailStr
from mixins import PasswordMixin, BaseEntity

class UserModel(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    phone: str
    email: Optional[EmailStr] = None
    date_of_birth: str
    is_active: bool
    role_id: int


class UserRegistrationModel(UserModel, PasswordMixin):
    is_active: bool = True


class UserLoginModel(PasswordMixin):
    phone: str


class UserAuthResponseModel(BaseEntity, UserModel):
    token: str
    token_type: str
