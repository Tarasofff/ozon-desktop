from typing import Callable
from PySide6.QtCore import Signal
from services.user.session.user_session_service import UserSessionService
from models import UserRegistrationModel, PaginatedRolesModel, UserAuthResponseModel
from services.user.api.user_api_service import UserApiService
from .base_viewmodel import BaseViewModel


class RegisterViewModel(BaseViewModel):
    roles_list = Signal(list)

    def __init__(self):
        super().__init__()
        self.user_api_service = UserApiService()
        self.user_session_service = UserSessionService()

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
        user = UserRegistrationModel.model_validate(
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

        auth_callback: Callable[[UserAuthResponseModel], None] = (
            lambda data: self.user_session_service.auth(data)
        )

        self._run_async_task(
            self.user_api_service.registration_request,
            user,
            success_callback=auth_callback,
            error_prefix="Ошибка регистрации",
        )

    def load_roles(self):
        roles_list_emit: Callable[[PaginatedRolesModel], None] = (
            lambda data: self.roles_list.emit(
                PaginatedRolesModel.model_validate(data).data
            )
        )

        self._run_async_task(
            self.user_api_service.get_all_user_roles_request,
            success_callback=roles_list_emit,
            error_prefix="Ошибка загрузки ролей",
        )
