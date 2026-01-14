from typing import Callable
from services.user.session.user_session_service import UserSessionService
from services.user.api.user_api_service import UserApiService
from .base_viewmodel import BaseViewModel
from models import UserLoginModel, UserAuthResponseModel


class LoginViewModel(BaseViewModel):

    def __init__(self):
        super().__init__()
        self.user_session_service = UserSessionService()
        self.user_api_service = UserApiService()

    def login(self, phone: str, password: str):
        payload = UserLoginModel(phone=phone, password=password)

        auth_callback: Callable[[UserAuthResponseModel], None] = (
            lambda data: self.user_session_service.auth(data)
        )

        self._run_async_task(
            self.user_api_service.login_request,
            payload,
            success_callback=auth_callback,
            error_prefix="Ошибка авторизации",
        )
