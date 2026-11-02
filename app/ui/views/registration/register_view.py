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
        self.first_name_input = FirstNameInput()
        self.last_name_input = LastNameInput()
        self.patronymic_input = PatronymicInput()
        self.email_input = EmailInput()
        self.phone_input = PhoneInput()
        self.date_of_birth_input = DateInput()

        self.role_selector = QComboBox()
        self.role_selector.addItem("Выберите роль", None)
        for role in UserRole:
            self.role_selector.addItem(role.value, role)

        self.password_input = PasswordInput()
        self.register_button = BaseButton("Зарегистрироваться")

    def _setup_layout(self):
        self.add(self.first_name_input)
        self.add(self.last_name_input)
        self.add(self.patronymic_input)
        self.add(self.email_input)
        self.add(self.phone_input)
        self.add(self.date_of_birth_input)
        self.add(self.role_selector)
        self.add(self.password_input)
        self.add(self.register_button)

    def _connect_signals(self):
        self.register_button.clicked.connect(self._handle_register)

    def _get_validated_user_account(self) -> UserAccount | None:
        if (
            not self.first_name_input.validate()
            or not self.last_name_input.validate()
            or not self.patronymic_input.validate()
            or not self.email_input.validate()
            or not self.phone_input.validate()
            or not self.password_input.validate()
        ):
            return None

        role_value = self.role_selector.currentData()

        if role_value is None:
            self.on_error("Выберите роль")
            return None

        return UserAccount(
            first_name=self.first_name_input.value(),
            last_name=self.last_name_input.value(),
            patronymic=self.patronymic_input.value(),
            email=self.email_input.value(),
            is_active=True,
            phone=self.phone_input.normalized_value(),
            password=self.password_input.value(),
            date_of_birth=self.date_of_birth_input.value(),
            role=UserRole(role_value),
        )

    def _handle_register(self):
        user_account = self._get_validated_user_account()

        if user_account is None:
            return

        profile_schema = CREATE_PROFILE_SCHEMAS[user_account.role]

        registration_data = UserCreate(user=user_account, profile=profile_schema())

        self.vm.registration(registration_data)
