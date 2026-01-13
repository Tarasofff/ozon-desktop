from pydantic import BaseModel
from typing import List
from mixins import PaginatedResponseMixin, BaseEntity


class RoleModel(BaseModel):
    name: str


class RoleResponseModel(BaseEntity, RoleModel):
    pass


class PaginatedRolesModel(PaginatedResponseMixin):
    data: List[RoleResponseModel]
