from schemas.shared import BaseCreate, BaseEntity, BaseSchema


class NurseBase(BaseSchema):
    pass


class NurseCreate(BaseCreate, NurseBase):
    pass


class NurseRead(BaseEntity, NurseBase):
    pass
