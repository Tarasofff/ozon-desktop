from PySide6.QtWidgets import QLineEdit, QPushButton
from ui.components import FormContainer
from viewmodels import LoginViewModel


class LoginView(FormContainer):
    def __init__(self):
        super().__init__("Вход")

        self.vm = LoginViewModel()

        self._create_widgets()
        self._setup_layout()
        self._connect_signals()

    def _create_widgets(self):
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Телефон")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Войти")

    def _setup_layout(self):
        self.add(self.phone_input)
        self.add(self.password_input)
        self.add(self.login_button)

    def _connect_signals(self):
        self.login_button.clicked.connect(self._handle_login)

    def _handle_login(self):
        phone = self.phone_input.text()
        password = self.password_input.text()

        self.vm.login(phone, password)
