from schemas.shared import BaseCreate, BaseEntity, BaseSchema


class DoctorBase(BaseSchema):
    pass


class DoctorCreate(BaseCreate, DoctorBase):
    pass


class DoctorRead(BaseEntity, DoctorBase):
    pass
