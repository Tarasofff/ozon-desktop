from pydantic import BaseModel
from models.mixins import PaginatedResponseMixin, BaseEntity


class RoleModel(BaseModel):
    name: str


class RoleEntityModel(BaseEntity, RoleModel):
    pass


class PaginatedRolesModel(PaginatedResponseMixin[RoleEntityModel]):
    pass
