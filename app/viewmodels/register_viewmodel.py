from PySide6.QtCore import QObject, Signal
import asyncio
from models.role_model import AllRolesResponseModel
from services.user.api.user_api_service import UserApiService


class RegisterViewModel(QObject):
    success = Signal()
    error = Signal(str)
    roles_list = Signal(list)

    def __init__(self):
        super().__init__()
        self.user_api_service = UserApiService()

    def register(self, phone: str, password: str):
        if not phone or not password:
            self.error.emit("Все поля обязательны")
        else:
            self.success.emit()

    def load_roles(self):
        asyncio.create_task(self._load_roles_task())

    async def _load_roles_task(self):
        try:
            ok, data = await self.user_api_service.get_all_user_roles()
            if ok:
                roles = AllRolesResponseModel.model_validate(data)
                self.roles_list.emit(roles.data)
            else:
                self.error.emit(f"Ошибка загрузки ролей: {data}")
        except Exception as e:
            self.error.emit(f"Ошибка сервера: {str(e)}")
