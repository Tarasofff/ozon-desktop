from typing import Optional
from pydantic import BaseModel
from models.mixins import PaginatedResponseMixin, BaseEntity


class PatientModel(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    phone: str
    date_of_birth: str
    email: Optional[str] = None
    is_active: Optional[bool]
    notes: Optional[str] = None


class PatientEntityModel(BaseEntity, PatientModel):
    pass


class PaginatedPatientsModel(PaginatedResponseMixin[PatientEntityModel]):
    pass
