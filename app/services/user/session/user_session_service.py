from infrastructure.storage.token_storage import delete_token, save_token
from infrastructure.storage.user_storage import delete_user, get_user, save_user
from models import UserModel, UserAuthResponseModel


class UserSessionService:
    def __init__(self):
        pass

    def auth(self, data: UserAuthResponseModel):
        try:
            auth_data = UserAuthResponseModel.model_validate(data)
            save_token(auth_data.token, auth_data.token_type)

            user_dict = auth_data.model_dump(include=set(UserModel.model_fields.keys()))
            user_data = UserModel(**user_dict)
            save_user(user_data)
        except Exception as e:
            self.logout()
            raise e

    def logout(self):
        delete_token()
        delete_user()

    def get_user(self):
        return get_user()
