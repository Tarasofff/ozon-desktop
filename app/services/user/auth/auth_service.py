from infrastructure.storage.token_storage import save_token
from models.user_model import UserLoginRequestSchema, UserLoginResponseSchema
from services.user.api.user_api_service import UserApiService


class AuthService:
    def __init__(self):
        self.user_api_service = UserApiService()

    async def auth(
        self, payload: UserLoginRequestSchema
    ) -> tuple[bool, UserLoginResponseSchema]:
        ok, data = await self.user_api_service.login_request(payload)

        if ok:
            user = UserLoginResponseSchema.model_validate(data)
            save_token(user.token)

        return ok, data
