from models.base_response_model import PaginatedResponseModel
from models.timestamp_model import Timestamp
from pydantic import BaseModel
from typing import List

class RoleEntity(Timestamp):
    id: int


class RoleModel(BaseModel):
    name: str


class RoleResponseModel(RoleEntity, RoleModel):
    pass


class AllRolesResponseModel(PaginatedResponseModel):
    data: List[RoleResponseModel]
