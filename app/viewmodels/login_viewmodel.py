import asyncio
from .base_viewmodel import BaseViewModel
from models import UserLoginModel
from services.user.auth.auth_service import AuthService


class LoginViewModel(BaseViewModel):

    def __init__(self):
        super().__init__()
        self.auth_service = AuthService()

    def login(self, phone: str, password: str):
        payload = UserLoginModel(phone=phone, password=password)
        asyncio.create_task(self._login_task(payload))

    async def _login_task(self, payload: UserLoginModel):
        try:
            ok, data = await self.auth_service.auth(payload)
            if ok:
                self.emit_success()
            else:
                self.emit_error(f"Ошибка входа: {data}")
        except Exception as e:
            self.emit_error(f"Ошибка сервера: {str(e)}")
