from PySide6.QtWidgets import QLineEdit
from ui.components.inputs.base_input import BaseInput


class PasswordInput(BaseInput):
    MIN_LENGTH = 4

    def __init__(
        self,
    ):
        super().__init__()
        self.setPlaceholderText("Пароль")
        self.setEchoMode(QLineEdit.EchoMode.Password)

    def value(self) -> str:
        return self.text()

    def validate(self) -> bool:
        password = self.value()

        error = None

        if not password:
            error = "Введите пароль"

        elif len(password) < self.MIN_LENGTH:
            error = f"Пароль должен содержать минимум {self.MIN_LENGTH} символов"

        self._set_error(error)

        return error is None
