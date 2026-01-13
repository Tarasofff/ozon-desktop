from typing import Optional
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt


class FormContainer(QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.setSpacing(15)

        self.error_label = QLabel("")
        self.error_label.setObjectName("error")

    def add(
        self,
        widget: QWidget,
        max_width: Optional[int] = 500,
        min_width: Optional[int] = None,
        max_height: Optional[int] = None,
        min_height: Optional[int] = None,
    ) -> None:
        if max_width:
            widget.setMaximumWidth(max_width)

        if min_width:
            widget.setMaximumHeight(min_width)

        if max_height:
            widget.setMaximumHeight(max_height)

        if min_height:
            widget.setMaximumHeight(min_height)

        self.main_layout.addWidget(widget)

    def on_success(self):
        self.error_label.setText("")

    def on_error(self, message: str):
        self.error_label.setText(message)
