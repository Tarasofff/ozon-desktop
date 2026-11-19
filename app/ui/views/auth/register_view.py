from PySide6.QtWidgets import (
    QComboBox,
)
from core.constants import UserRole
from schemas.doctor import DoctorCreate
from schemas.nurse import NurseCreate
from schemas.user import UserAccount, UserCreate
from ui.components.buttons import BaseButton
from ui.components.inputs import (
    EmailInput,
    FirstNameInput,
    LastNameInput,
    PasswordInput,
    PatronymicInput,
    PhoneInput,
    DateInput,
)
from viewmodels import RegisterViewModel
from ui.views.base.form_container_view import FormContainerView

CREATE_PROFILE_SCHEMAS = {
    UserRole.NURSE: NurseCreate,
    UserRole.DOCTOR: DoctorCreate,
}


class RegisterView(FormContainerView):
    def __init__(self):
        super().__init__("Регистрация")

        self.vm = RegisterViewModel()

        self._create_widgets()
        self._setup_layout()
        self._connect_signals()

    def _create_widgets(self):
        self._first_name_input = FirstNameInput()
        self._last_name_input = LastNameInput()
        self._patronymic_input = PatronymicInput()
        self._email_input = EmailInput()
        self._phone_input = PhoneInput()
        self._date_of_birth_input = DateInput()

        self._role_selector = QComboBox()
        self._role_selector.addItem("Выберите роль", None)
        for role in UserRole:
            self._role_selector.addItem(role.value, role)

        self._password_input = PasswordInput()
        self._register_button = BaseButton("Зарегистрироваться")

    def _setup_layout(self):
        self.add(self._first_name_input)
        self.add(self._last_name_input)
        self.add(self._patronymic_input)
        self.add(self._email_input)
        self.add(self._phone_input)
        self.add(self._date_of_birth_input)
        self.add(self._role_selector)
        self.add(self._password_input)
        self.add(self._register_button)

    def _connect_signals(self):
        self._register_button.clicked.connect(self._handle_registration)

    def _get_validated_user_account(self) -> UserAccount | None:
        if (
            not self._first_name_input.validate()
            or not self._last_name_input.validate()
            or not self._patronymic_input.validate()
            or not self._email_input.validate()
            or not self._phone_input.validate()
            or not self._password_input.validate()
        ):
            return None

        role_value = self._role_selector.currentData()

        if role_value is None:
            return None

        return UserAccount(
            first_name=self._first_name_input.value(),
            last_name=self._last_name_input.value(),
            patronymic=self._patronymic_input.value(),
            email=self._email_input.value(),
            is_active=True,
            phone=self._phone_input.normalized_value(),
            password=self._password_input.value(),
            date_of_birth=self._date_of_birth_input.value(),
            role=UserRole(role_value),
        )

    def _handle_registration(self):
        user_account = self._get_validated_user_account()

        if user_account is None:
            return

        profile_schema = CREATE_PROFILE_SCHEMAS[user_account.role]

        registration_data = UserCreate(user=user_account, profile=profile_schema())

        self.vm.registration(registration_data)
