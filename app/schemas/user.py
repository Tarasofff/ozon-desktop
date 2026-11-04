from datetime import date
from pydantic import EmailStr
from core.constants.user_role import UserRole
from schemas.doctor import DoctorCreate
from schemas.nurse import NurseCreate
from schemas.shared.base_create import BaseCreate
from schemas.shared.base_read import BaseRead
from schemas.shared.base_schema import BaseSchema
from schemas.shared.types.auth import PasswordStr
from schemas.shared.types.user_identity import (
    FirstNameStr,
    LastNameStr,
    PatronymicStr,
    PhoneStr,
)


class UserBase(BaseSchema):
    first_name: FirstNameStr
    patronymic: PatronymicStr
    last_name: LastNameStr
    phone: PhoneStr
    email: EmailStr | None = None
    date_of_birth: date
    is_active: bool
    role: UserRole


class UserAccount(BaseCreate, UserBase):
    password: PasswordStr


class UserCreate(BaseCreate):
    user: UserAccount
    profile: DoctorCreate | NurseCreate


class UserRead(BaseRead, UserBase):
    pass
