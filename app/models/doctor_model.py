from pydantic import BaseModel
from models.mixins import PaginatedResponseMixin, BaseEntity


class DoctorSpecializationModel(BaseModel):
    name: str


class DoctorSpecializationEntityModel(BaseEntity, DoctorSpecializationModel):
    pass


class PaginatedDoctorSpecializationModel(
    PaginatedResponseMixin[DoctorSpecializationEntityModel]
):
    pass
