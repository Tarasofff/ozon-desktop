from typing import List
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QDateEdit, QComboBox
from models.role_model import RoleResponseModel
from viewmodels.register_viewmodel import RegisterViewModel
from ui.components.forms.form_container import FormContainer
from ui.components.buttons.back_button import BackButton
from PySide6.QtCore import Qt, QDate


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

        self.error_label = QLabel("")
        self.error_label.setObjectName("error")

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

        self.vm.success.connect(self._on_success)
        self.vm.error.connect(self._on_error)

        self.vm.roles_list.connect(self._on_roles_loaded)

    def _handle_register(self):
        first_name = self.first_name_input.text()
        middle_name = self.middle_name_input.text()
        last_name = self.last_name_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()
        password = self.password_input.text()
        # self.vm.register(phone, password)

    def _on_success(self):
        self.error_label.setText("")
        print("Успешная регистрация!")

    def _on_error(self, message: str):
        self.error_label.setText(message)
        print("Ошибка регистрации:", message)
