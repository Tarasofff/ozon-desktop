from PySide6.QtCore import QObject, Signal
import asyncio
from models.user_model import UserLoginRequestSchema
from services.user.auth.auth_service import AuthService


class LoginViewModel(QObject):
    success = Signal()
    error = Signal(str)

    def __init__(self):
        super().__init__()
        self.auth_service = AuthService()

    def login(self, phone: str, password: str):
        if not phone or not password:
            self.error.emit("Заполните все поля")
            return

        payload = UserLoginRequestSchema(phone=phone, password=password)

        asyncio.create_task(self._login_task(payload))

    async def _login_task(self, payload: UserLoginRequestSchema):
        try:
            ok, data = await self.auth_service.auth(payload)
            if ok:
                self.success.emit()
            else:
                self.error.emit(f"Ошибка входа: {data}")
        except Exception as e:
            self.error.emit(f"Ошибка сервера: {str(e)}")
