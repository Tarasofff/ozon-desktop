from datetime import date
from pydantic import EmailStr
from app.core.constants.user_role import UserRole
from app.schemas.doctor import DoctorCreate
from app.schemas.nurse import NurseCreate
from app.schemas.shared.base_create import BaseCreate
from app.schemas.shared.base_read import BaseRead
from app.schemas.shared.base_schema import BaseSchema
from app.schemas.shared.types.auth import PasswordStr
from app.schemas.shared.types.identity import (
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
    is_active: bool = True
    hospital_id: int
    role: UserRole


class UserAccount(BaseCreate, UserBase):
    password: PasswordStr


class UserCreate(BaseCreate):
    user: UserAccount
    profile: DoctorCreate | NurseCreate


class UserRead(BaseRead, UserBase):
    pass
