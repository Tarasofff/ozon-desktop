from pydantic import BaseModel


class PasswordMixin(BaseModel):
    password: str
