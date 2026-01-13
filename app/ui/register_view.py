from typing import List
from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QDateEdit,
    QComboBox,
)
from models import RoleResponseModel
from viewmodels import RegisterViewModel
from components import FormContainer, BackButton
from PySide6.QtCore import Qt, QDate
import re

class RegisterView(FormContainer):
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

        self.middle_name_input = QLineEdit()
        self.middle_name_input.setPlaceholderText("Фамилия")

        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText("Отчество")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Телефон")

        self.date_of_birth_input = QDateEdit()
        self.date_of_birth_input.setDisplayFormat("yyyy-MM-dd")
        self.date_of_birth_input.setCalendarPopup(True)
        self.date_of_birth_input.setDate(QDate.currentDate())

        self.role_selector = QComboBox()
        self.role_selector.setPlaceholderText("Выберите роль")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.register_button = QPushButton("Зарегестрироваться")

    def _setup_layout(self):
        self.add(self.title_label)
        self.add(self.first_name_input)
        self.add(self.middle_name_input)
        self.add(self.last_name_input)
        self.add(self.email_input)
        self.add(self.phone_input)
        self.add(self.date_of_birth_input)
        self.add(self.role_selector)
        self.add(self.password_input)
        self.add(self.register_button)
        self.add(self.error_label)
        self.add(self.back_button)

    def _on_roles_loaded(self, roles: List[RoleResponseModel]):
        self.role_selector.clear()

        for role in roles:
            self.role_selector.addItem(role.name, role.id)

    def _connect_signals(self):
        self.register_button.clicked.connect(self._handle_register)

        self.vm.success.connect(self.on_success)
        self.vm.error.connect(self.on_error)

        self.vm.roles_list.connect(self._on_roles_loaded)

    def _validate_inputs(self) -> bool:
        first_name = self.first_name_input.text().strip()
        middle_name = self.middle_name_input.text().strip()
        last_name = self.last_name_input.text().strip()
        email = self.email_input.text().strip()
        phone = self.phone_input.text().strip()
        password = self.password_input.text()
        role_id = self.role_selector.currentData()

        # Проверка имени, фамилии, отчества (только буквы)
        name_pattern = re.compile(r"^[A-Za-zА-Яа-яЁё]+$")
        for field_name, value in [
            ("Имя", first_name),
            ("Фамилия", middle_name),
            ("Отчество", last_name),
        ]:
            if not value:
                self.on_error(f"{field_name} обязательное поле")
                return False
            if not name_pattern.match(value):
                self.on_error(f"{field_name} должно содержать только буквы")
                return False

        # Проверка email (простейший regex)
        email_pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
        if email and not email_pattern.match(email):
            self.on_error("Неверный формат email")
            return False

        # Проверка телефона (только цифры)
        if not phone:
            self.on_error("Телефон обязателен")
            return False
        if not phone.isdigit():
            self.on_error("Телефон должен содержать только цифры")
            return False

        # Проверка пароля
        if not password:
            self.on_error("Пароль обязателен")
            return False

        # Проверка роли
        if role_id is None:
            self.on_error("Выберите роль")
            return False

        # Все проверки пройдены
        self.on_success()
        return True

    def _handle_register(self):
        if not self._validate_inputs():
            return

        first_name = self.first_name_input.text()
        middle_name = self.middle_name_input.text()
        last_name = self.last_name_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()
        password = self.password_input.text()
        dob = self.date_of_birth_input.text()
        role_id = self.role_selector.currentData()

        print(
            7777,
            {
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
                "email": email,
                "phone": phone,
                "password": password,
                "date_of_birth": dob,
                "role_id": role_id,
            },
        )

        self.vm.register(
            first_name,
            middle_name,
            last_name,
            email,
            phone,
            password,
            dob,
            role_id,
        )
