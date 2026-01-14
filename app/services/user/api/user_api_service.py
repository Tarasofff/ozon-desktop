from core.constants import UserApi
from models.role_model import PaginatedRolesModel
from models import (
    UserLoginModel,
    UserAuthResponseModel,
    UserRegistrationModel,
)
from infrastructure.http.client import http


class UserApiService:

    async def login_request(
        self, data: UserLoginModel
    ) -> tuple[bool, UserAuthResponseModel]:
        response = await http.post(
            UserApi.login,
            json=data.model_dump(),
        )

        return response.status_code == 200, response.json()

    async def registration_request(
        self, data: UserRegistrationModel
    ) -> tuple[bool, UserAuthResponseModel]:
        response = await http.post(
            UserApi.register,
            json=data.model_dump(),
        )

        return response.status_code == 201, response.json()

    async def get_all_user_roles(
        self, limit: int = 15, offset: int = 0
    ) -> tuple[bool, PaginatedRolesModel]:
        response = await http.get(
            UserApi.get_all_roles(limit, offset),
        )

        return response.status_code == 200, response.json()
