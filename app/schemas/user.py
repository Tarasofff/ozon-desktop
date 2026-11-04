from datetime import date
from pydantic import EmailStr
from schemas.doctor import DoctorCreate
from schemas.nurse import NurseCreate
from core.constants import UserRole
from schemas.shared import BaseSchema, BaseCreate, BaseEntity
from schemas.shared.types.auth import PasswordStr
from schemas.shared.types import (
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


class UserRead(BaseEntity, UserBase):
    pass
