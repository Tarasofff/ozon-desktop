import re
from ui.components.inputs.base_input import BaseInput


class PhoneInput(BaseInput):
    PHONE_PATTERN = re.compile(r"^\+?[0-9]{10,15}$")

    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Телефон")

    def value(self) -> str:
        return self.text().strip()

    def normalized_value(self) -> str:
        return re.sub(r"[\s()-]", "", self.value())

    def validate(self) -> bool:
        phone = self.normalized_value()

        error = None

        if not phone:
            error = "Введите номер телефона"

        elif not self.PHONE_PATTERN.fullmatch(phone):
            error = "Введите корректный номер телефона"

        self._set_error(error)

        return error is None
