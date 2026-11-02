import re
from ui.components.inputs.base_input import BaseInput


class EmailInput(BaseInput):
    EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Электронная почта")

    def value(self) -> str | None:
        return self.text().strip() or None

    def validate(self) -> bool:
        email = self.value()

        error = None

        if email and not self.EMAIL_PATTERN.fullmatch(email):
            error = "Введите корректный адрес электронной почты"

        self._set_error(error)

        return error is None
