from pydantic import BaseModel
from models.mixins import PaginatedResponseMixin, BaseEntity


class RoleModel(BaseModel):
    name: str


class RoleResponseModel(BaseEntity, RoleModel):
    pass


class PaginatedRolesModel(PaginatedResponseMixin[RoleResponseModel]):
    pass
