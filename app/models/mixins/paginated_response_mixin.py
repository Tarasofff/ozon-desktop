from pydantic import BaseModel


class PaginatedResponseMixin(BaseModel):
    total: int
    limit: int
    offset: int
