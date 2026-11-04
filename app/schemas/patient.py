from datetime import date
from pydantic import BaseModel, EmailStr
from schemas.shared import BaseEntity, PaginatedResponse
from schemas.shared.types import (
    FirstNameStr,
    LastNameStr,
    PatronymicStr,
    PhoneStr,
)


class PatientBase(BaseModel):
    first_name: FirstNameStr
    patronymic: PatronymicStr
    last_name: LastNameStr
    phone: PhoneStr
    date_of_birth: date
    email: EmailStr | None = None
    is_active: bool
    notes: str | None = None


# class TreatmentPlan(BaseCreate):
#     diagnose_id: int
#     planned_session_count: int


# class PatientCreate(BaseCreate, PatientBase):
#     user_id: int
#     diagnose_ids: Optional[list[TreatmentPlan]]


class PatientRead(PatientBase, BaseEntity):
    pass


class PaginatedPatientsResponse(PaginatedResponse[PatientRead]):
    pass
