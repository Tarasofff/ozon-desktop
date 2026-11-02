from typing import Optional
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from ui.components.buttons import BackButton
from schemas.shared import ViewModelProtocol


class FormContainer(QWidget):
    def __init__(self, title: str):
        super().__init__()

        self.back_button = BackButton()

        self.title_label = QLabel(title)
        self.title_label.setObjectName("title")

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.setSpacing(15)
        self.main_layout.addWidget(self.title_label)

        self.error_label = QLabel()
        self.error_label.setObjectName("error")

        self._setup_default_layout()

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

    def on_success(self, message: str = ""):
        self.error_label.setText(message)

    def on_error(self, message: str):
        self.error_label.setText(message)

    def _setup_default_layout(self) -> None:
        self.add(self.error_label)
        self.add(self.back_button)

    def connect_viewmodel(self, vm: ViewModelProtocol) -> None:
        vm.success.connect(self.on_success)
        vm.error.connect(self.on_error)
