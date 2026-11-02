from schemas.shared.base_schema import BaseSchema
from schemas.shared import BaseCreate, BaseRead


class NurseBase(BaseSchema):
    pass


class NurseCreate(BaseCreate, NurseBase):
    pass


class NurseRead(BaseRead, NurseBase):
    pass
