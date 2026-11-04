from services.auth.auth_api_service import AuthApiService
from services.session.session_service import SessionService
from schemas.auth import AuthPayload
from .base_viewmodel import BaseViewModel


class LoginViewModel(BaseViewModel):

    def __init__(self):
        super().__init__()
        self.auth_api_service = AuthApiService()
        self.session_service = SessionService()

    def login(self, data: AuthPayload):
        self.run_async_task(
            self.auth_api_service.login,
            data,
            success_callback=self.session_service.save_session,
            error_prefix="Ошибка авторизации",
        )
