import re
from datetime import date
from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QDateEdit,
    QComboBox,
)
from app.core.constants import UserRole
from app.schemas.doctor import DoctorCreate
from app.schemas.nurse import NurseCreate
from app.schemas.user import UserAccount, UserCreate
from viewmodels import RegisterViewModel
from ui.components import FormContainer, BackButton
from PySide6.QtCore import Qt, QDate

PROFILE_SCHEMAS = {
    UserRole.NURSE: NurseCreate,
    UserRole.DOCTOR: DoctorCreate,
}


# TODO: Implement the registration logic in the RegisterViewModel and connect it to the UI.
class RegisterView(FormContainer):
    NAME_PATTERN = re.compile(r"^[A-Za-zА-Яа-яЁёІіЇїЄєҐґ'-]+$")
    EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def __init__(self):
        super().__init__()

        self.vm = RegisterViewModel()
        self.back_button = BackButton()

        self._create_widgets()
        self._setup_layout()
        self._connect_signals()

    def _create_widgets(self):
        self.title_label = QLabel("Регистрация")
        self.title_label.setObjectName("title")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.first_name_input = QLineEdit()
        self.first_name_input.setPlaceholderText("Имя")

        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText("Фамилия")

        self.patronymic_input = QLineEdit()
        self.patronymic_input.setPlaceholderText("Отчество")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Телефон")

        self.date_of_birth_input = QDateEdit()
        self.date_of_birth_input.setDisplayFormat("yyyy-MM-dd")
        self.date_of_birth_input.setCalendarPopup(True)
        self.date_of_birth_input.setDate(QDate.currentDate())
        self.date_of_birth_input.setMaximumDate(QDate.currentDate())

        self.role_selector = QComboBox()
        self.role_selector.addItem("Выберите роль", None)

        for role in UserRole:
            self.role_selector.addItem(role.value, role)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.register_button = QPushButton("Зарегистрироваться")

    def _setup_layout(self):
        self.add(self.title_label)
        self.add(self.first_name_input)
        self.add(self.last_name_input)
        self.add(self.patronymic_input)
        self.add(self.email_input)
        self.add(self.phone_input)
        self.add(self.date_of_birth_input)
        self.add(self.role_selector)
        self.add(self.password_input)
        self.add(self.register_button)
        self.add(self.error_label)
        self.add(self.back_button)

    def _connect_signals(self):
        self.register_button.clicked.connect(self._handle_register)

        self.vm.success.connect(self.on_success)
        self.vm.error.connect(self.on_error)

    def _get_validated_user_account(self) -> UserAccount | None:
        first_name = self.first_name_input.text().strip()
        last_name = self.last_name_input.text().strip()
        patronymic = self.patronymic_input.text().strip()
        email = self.email_input.text().strip()
        phone = self.phone_input.text().strip()
        password = self.password_input.text()
        role_value = self.role_selector.currentData()

        qdate = self.date_of_birth_input.date()
        date_of_birth = date(
            qdate.year(),
            qdate.month(),
            qdate.day(),
        )

        # TODO
        names = (
            ("Имя", first_name),
            ("Фамилия", last_name),
            ("Отчество", patronymic),
        )

        for field_name, value in names:
            if not value:
                self.on_error(f"{field_name} — обязательное поле")
                return None

            if not self.NAME_PATTERN.fullmatch(value):
                self.on_error(f"{field_name}: проверьте введённые символы")
                return None

        if email and not self.EMAIL_PATTERN.fullmatch(email):
            self.on_error("Неверный формат email")
            return None

        if not phone:
            self.on_error("Телефон обязателен")
            return None

        normalized_phone = phone.replace(" ", "").replace("-", "")

        if not re.fullmatch(r"\+?\d{10,15}", normalized_phone):
            self.on_error("Проверьте формат телефона")
            return None

        if not password:
            self.on_error("Пароль обязателен")
            return None

        if role_value is None:
            self.on_error("Выберите роль")
            return None

        return UserAccount(
            first_name=first_name,
            last_name=last_name,
            patronymic=patronymic,
            email=email or None,
            is_active=True,
            hospital_id=1,  # TODO: определить больницу
            phone=normalized_phone,
            password=password,
            date_of_birth=date_of_birth,
            role=UserRole(role_value),
        )

    def _handle_register(self):
        user_account = self._get_validated_user_account()

        if user_account is None:
            return

        profile_schema = PROFILE_SCHEMAS[user_account.role]

        registration_data = UserCreate(user=user_account, profile=profile_schema())

        self.vm.registration(registration_data)
