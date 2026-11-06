from typing import Optional
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QScrollArea,
)
from PySide6.QtCore import Qt
from ui.components.buttons import BackButton


class FormContainerView(QWidget):
    def __init__(self, title: str):
        super().__init__()

        self._create_base_widgets(title)
        self._setup_base_layout()

    def _create_base_widgets(self, title: str):
        self.back_button = BackButton()

        self._title_label = QLabel(title)
        self._title_label.setObjectName("title")

        self._content_widget = QWidget()
        self._content_widget.setObjectName("formContent")

        self.content_layout = QVBoxLayout(self._content_widget)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_layout.setSpacing(15)

        self._scroll_area = QScrollArea()
        self._scroll_area.setObjectName("formScrollArea")
        self._scroll_area.setWidgetResizable(True)
        self._scroll_area.setFrameShape(QScrollArea.Shape.NoFrame)
        self._scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self._scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        self._scroll_area.setWidget(self._content_widget)

        self._main_layout = QVBoxLayout(self)
        self._main_layout.setSpacing(15)
        self._main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._main_layout.addWidget(self._title_label)
        self._main_layout.addWidget(self._scroll_area, 1)

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

    def _setup_base_layout(self) -> None:
        self.add(self.back_button)
