from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton
from components import FormContainer, BackButton
from viewmodels import LoginViewModel
from PySide6.QtCore import Qt


class LoginView(FormContainer):
    def __init__(self):
        super().__init__()
        self.vm = LoginViewModel()
        self.back_button = BackButton()

        self._create_widgets()
        self._setup_layout()
        self._connect_signals()

    def _create_widgets(self):
        self.title_label = QLabel("Вход")
        self.title_label.setObjectName("title")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Телефон")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Войти")

    def _setup_layout(self):
        self.add(self.title_label)
        self.add(self.phone_input)
        self.add(self.password_input)
        self.add(self.login_button)
        self.add(self.error_label)
        self.add(self.back_button)

    def _connect_signals(self):
        self.login_button.clicked.connect(self._handle_login)
        self.vm.success.connect(self.on_success)
        self.vm.error.connect(self.on_error)

    def _handle_login(self):
        phone = self.phone_input.text()
        password = self.password_input.text()

        self.vm.login(phone, password)
