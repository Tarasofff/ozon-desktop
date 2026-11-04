from schemas.user import UserCreate
from services.session.session_service import SessionService
from services.user.user_api_service import UserApiService
from .base_viewmodel import BaseViewModel


class RegisterViewModel(BaseViewModel):
    def __init__(self):
        super().__init__()
        self.user_api_service = UserApiService()
        self.session_service = SessionService()

    def registration(self, data: UserCreate):
        self.run_async_task(
            self.user_api_service.registration,
            data,
            success_callback=self.session_service.save_session,
            error_prefix="Ошибка регистрации",
        )
