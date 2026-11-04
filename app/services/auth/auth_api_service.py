from infrastructure.api.http_client import http_client
from schemas.auth import AuthPayload, AuthResponse
from infrastructure.api.routes import auth_api


class AuthApiService:
    async def login(self, data: AuthPayload) -> AuthResponse:
        response = await http_client.post(
            auth_api.LOGIN,
            json=data.model_dump(mode="json"),
        )
        response.raise_for_status()

        return AuthResponse.model_validate(response.json())
