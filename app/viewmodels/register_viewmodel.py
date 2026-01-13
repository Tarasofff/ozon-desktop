from PySide6.QtCore import Signal
import asyncio
from models import UserRegistrationModel, PaginatedRolesModel
from services.user.api.user_api_service import UserApiService
from .base_viewmodel import BaseViewModel


class RegisterViewModel(BaseViewModel):
    roles_list = Signal(list)

    def __init__(self):
        super().__init__()
        self.user_api_service = UserApiService()

    def register(
        self,
        first_name: str,
        middle_name: str,
        last_name: str,
        email: str,
        phone: str,
        password: str,
        date_of_birth: str,
        role_id: int,
    ):
        payload = UserRegistrationModel.model_validate(
            {
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
                "email": email or None,
                "phone": phone,
                "password": password,
                "date_of_birth": date_of_birth,
                "role_id": role_id,
            }
        )

        asyncio.create_task(self._register_task(payload))

    def load_roles(self):
        asyncio.create_task(self._load_roles_task())

    async def _register_task(self, user: UserRegistrationModel):
        try:
            ok, data = await self.user_api_service.registration_request(user)
            if ok:
                self.emit_success()
            else:
                self.emit_error(f"Ошибка регистрации: {data}")
        except Exception as e:
            self.emit_error(f"Ошибка сервера: {str(e)}")

    async def _load_roles_task(self):
        try:
            ok, data = await self.user_api_service.get_all_user_roles()
            if ok:
                roles = PaginatedRolesModel.model_validate(data)
                self.emit_success()
                self.roles_list.emit(roles.data)
            else:
                self.emit_error(f"Ошибка загрузки ролей: {data}")
        except Exception as e:
            self.emit_error(f"Ошибка сервера: {str(e)}")
