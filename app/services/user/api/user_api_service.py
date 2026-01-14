from core.constants import user_api
from models import (
    UserLoginModel,
    UserAuthResponseModel,
    UserRegistrationModel,
    PaginatedRolesModel,
)
from infrastructure.http.client import http


class UserApiService:

    async def login_request(
        self, data: UserLoginModel
    ) -> tuple[bool, UserAuthResponseModel]:
        response = await http.post(
            user_api.LOGIN,
            json=data.model_dump(),
        )

        return response.status_code == 200, response.json()

    async def registration_request(
        self, data: UserRegistrationModel
    ) -> tuple[bool, UserAuthResponseModel]:
        response = await http.post(
            user_api.REGISTRATION,
            json=data.model_dump(),
        )

        return response.status_code == 201, response.json()

    async def get_all_user_roles_request(
        self, limit: int = 15, offset: int = 0
    ) -> tuple[bool, PaginatedRolesModel]:
        response = await http.get(
            user_api.get_all_roles(limit, offset),
        )

        return response.status_code == 200, response.json()
