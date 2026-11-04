from core.config.app_config import app_config


class BaseApi:
    _PREFIX = f"{app_config.api_url_v1}"

    def _pagination(self, limit: int, offset: int) -> str:
        return f"limit={limit}&offset={offset}"


class UserApi(BaseApi):

    def __init__(self):
        self.INDEX = f"{self._PREFIX}/user"
        self.REGISTRATION = f"{self.INDEX}/create"


class AuthApi(BaseApi):

    def __init__(self):
        self.INDEX = f"{self._PREFIX}/auth"
        self.LOGIN = f"{self.INDEX}/login"


user_api = UserApi()
auth_api = AuthApi()
