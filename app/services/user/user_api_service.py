from schemas.auth import AuthResponse
from schemas.user import UserCreate
from infrastructure.api.http_client import http_client
from infrastructure.api.routes import user_api


class UserApiService:
    async def registration(self, data: UserCreate) -> AuthResponse:
        response = await http_client.post(
            user_api.REGISTRATION,
            json=data.model_dump(mode="json"),
        )
        response.raise_for_status()


        return AuthResponse.model_validate(response.json())
