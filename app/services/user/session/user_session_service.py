from infrastructure.storage.token_storage import delete_token, save_token
from infrastructure.storage.user_storage import delete_user, get_user, save_user
from schemas import UserBase, AuthResponse


class UserSessionService:
    def __init__(self):
        pass

    def auth(self, data: AuthResponse):
        try:
            auth_data = AuthResponse.model_validate(data)
            save_token(auth_data.token.access_token, auth_data.token.token_type)

            user_dict = auth_data.model_dump(include=set(UserBase.model_fields.keys()))
            user_data = UserBase(**user_dict)
            save_user(user_data)
        except Exception as e:
            self.logout()
            raise e

    def logout(self):
        delete_token()
        delete_user()

    def get_user(self):
        return get_user()
