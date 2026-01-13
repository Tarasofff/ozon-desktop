from infrastructure.storage.token_storage import save_token
from models.user_model import UserLoginModel, UserAuthResponseModel
from services.user.api.user_api_service import UserApiService


class AuthService:
    def __init__(self):
        self.user_api_service = UserApiService()

    async def auth(self, payload: UserLoginModel) -> tuple[bool, UserAuthResponseModel]:
        ok, data = await self.user_api_service.login_request(payload)

        if ok:
            user = UserAuthResponseModel.model_validate(data)
            # save_token(user.token)

        return ok, data
