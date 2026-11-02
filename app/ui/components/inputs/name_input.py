import re
from ui.components.inputs.base_input import BaseInput


class NameInput(BaseInput):
    NAME_PATTERN = re.compile(
        r"^[A-Za-zА-Яа-яЁёІіЇїЄєҐґ]+(?:[ '\u2019-][A-Za-zА-Яа-яЁёІіЇїЄєҐґ]+)*$"
    )
    MIN_LENGTH = 2

    def __init__(
        self,
        placeholder: str,
    ):
        super().__init__()
        self.setPlaceholderText(placeholder)

    def value(self) -> str:
        return self.text().strip()

    def validate(self) -> bool:
        name = self.value()

        error = None

        if not name:
            error = f"Поле «{self.placeholderText()}» обязательно для заполнения"

        elif name and len(name) < self.MIN_LENGTH:
            error = (
                f"Поле «{self.placeholderText()}» "
                f"должно содержать минимум {self.MIN_LENGTH} символа"
            )

        elif name and not self.NAME_PATTERN.fullmatch(name):
            error = (
                f"Поле «{self.placeholderText()}» "
                "может содержать только буквы, дефис и апостроф"
            )

        self._set_error(error)

        return error is None
