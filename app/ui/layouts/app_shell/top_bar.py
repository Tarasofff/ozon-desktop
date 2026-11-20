from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QWidget,
)

from ui.components.buttons.base_button import BaseButton


class TopBar(QFrame):
    profile_requested = Signal()

    HEIGHT = 72

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._setup_ui()
        self._setup_signals()

    def _setup_ui(self) -> None:
        self.setObjectName("topBar")
        self.setFixedHeight(self.HEIGHT)

        self._layout = QHBoxLayout(self)
        self._layout.setContentsMargins(28, 0, 28, 0)

        self._create_page_title()
        self._create_profile_button()

    def _create_page_title(self) -> None:
        self._page_title = QLabel("Главная")
        self._page_title.setObjectName("pageTitle")

        self._layout.addWidget(self._page_title)
        self._layout.addStretch()

    def _create_profile_button(self) -> None:
        self._profile_button = BaseButton("Мой профиль  ▾")
        self._profile_button.setObjectName("profileButton")
        self._profile_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self._profile_button.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed,
        )

        self._layout.addWidget(self._profile_button)

    def _setup_signals(self) -> None:
        self._profile_button.btn_clicked.connect(self.profile_requested.emit)

    def set_page_title(self, title: str) -> None:
        self._page_title.setText(title)
