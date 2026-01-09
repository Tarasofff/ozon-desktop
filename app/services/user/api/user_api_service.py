from models.role_model import AllRolesResponseModel
from models.user_model import UserLoginRequestSchema, UserLoginResponseSchema
from core.api_routes import user_api
from infrastructure.http.client import http


class UserApiService:
    async def login_request(
        self, data: UserLoginRequestSchema
    ) -> tuple[bool, UserLoginResponseSchema]:
        response = await http.post(
            user_api.login,
            json=data.model_dump(),
        )

        return response.status_code == 200, response.json()

    async def get_all_user_roles(
        self, limit: int = 15, offset: int = 0
    ) -> tuple[bool, AllRolesResponseModel]:
        response = await http.get(
            user_api.get_all_roles(limit, offset),
        )

        return response.status_code == 200, response.json()
