from typing import Optional
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QScrollArea,
)
from PySide6.QtCore import Qt
from ui.components.buttons import BackButton
from schemas.shared import ViewModelProtocol


class FormContainerView(QWidget):
    def __init__(self, title: str):
        super().__init__()

        self.back_button = BackButton()

        self.title_label = QLabel(title)
        self.title_label.setObjectName("title")

        self.content_widget = QWidget()
        self.content_widget.setObjectName("formContent")
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_layout.setSpacing(15)

        self.scroll_area = QScrollArea()
        self.scroll_area.setObjectName("formScrollArea")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QScrollArea.Shape.NoFrame)
        self.scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        self.scroll_area.setWidget(self.content_widget)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setSpacing(15)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.title_label)
        self.main_layout.addWidget(self.scroll_area, 1)

        self.error_label = QLabel()
        self.error_label.setObjectName("error")

        self._setup_default_layout()

    def add(
        self,
        widget: QWidget,
        max_width: Optional[int] = 500,
        min_width: Optional[int] = 500,
        max_height: Optional[int] = None,
        min_height: Optional[int] = None,
    ) -> None:
        if max_width is not None:
            widget.setMaximumWidth(max_width)

        if min_width is not None:
            widget.setMinimumWidth(min_width)

        if max_height is not None:
            widget.setMaximumHeight(max_height)

        if min_height is not None:
            widget.setMinimumHeight(min_height)

        index = self.content_layout.indexOf(self.back_button)
        self.content_layout.insertWidget(
            index, widget, alignment=Qt.AlignmentFlag.AlignHCenter
        )

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
