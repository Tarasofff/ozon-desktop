from PySide6.QtWidgets import QLineEdit, QSizePolicy


class BaseInput(QLineEdit):
    def __init__(self):
        super().__init__()
        self.textChanged.connect(self._clear_error)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )

    def _set_error(self, message: str | None) -> None:
        self.setProperty("error", message is not None)
        self.setToolTip(message or "")

        self.style().unpolish(self)
        self.style().polish(self)

    def _clear_error(self) -> None:
        if self.property("error"):
            self._set_error(None)
