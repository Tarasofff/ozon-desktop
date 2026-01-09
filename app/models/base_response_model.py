from pydantic import BaseModel


class PaginatedResponseModel(BaseModel):
    total: int
    limit: int
    offset: int
