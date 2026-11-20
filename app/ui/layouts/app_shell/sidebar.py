from enum import StrEnum

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from ui.components.buttons.base_button import BaseButton
from ui.layouts.app_shell.navigation_menu import NavMenu


class Sidebar(QWidget):
    SIDEBAR_WIDTH = 240

    navigation_requested = Signal(object)
    settings_requested = Signal()
    logout_requested = Signal()

    def __init__(
        self,
        nav_items: list[tuple[StrEnum, str]],
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)

        self._nav_items = nav_items

        self._setup_ui()
        self._setup_signals()

    def _setup_ui(self) -> None:
        self.setObjectName("sidebar")
        self.setFixedWidth(self.SIDEBAR_WIDTH)

        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(16, 24, 16, 20)
        self._layout.setSpacing(8)

        self._create_brand()
        self._create_navigation()
        self._create_actions()

    def _create_brand(self) -> None:
        self._brand_label = QLabel("OZON DESKTOP")
        self._brand_label.setObjectName("brandLabel")

        self._layout.addWidget(self._brand_label)
        self._layout.addSpacing(28)

    def _create_navigation(self) -> None:
        self._nav_menu = NavMenu(self._nav_items)
        self._layout.addWidget(self._nav_menu)

        self._layout.addStretch()

    def _create_actions(self) -> None:
        self._settings_button = BaseButton("Настройки")
        self._settings_button.setObjectName("navButton")
        self._settings_button.setCursor(Qt.CursorShape.PointingHandCursor)

        self._logout_button = BaseButton("Выйти")
        self._logout_button.setObjectName("logoutButton")
        self._logout_button.setCursor(Qt.CursorShape.PointingHandCursor)

        self._layout.addWidget(self._settings_button)
        self._layout.addWidget(self._logout_button)

    def _setup_signals(self) -> None:
        self._nav_menu.navigation_requested.connect(self.navigation_requested.emit)

        self._settings_button.btn_clicked.connect(self.settings_requested.emit)

        self._logout_button.btn_clicked.connect(self.logout_requested.emit)

    def set_active_route(self, route: StrEnum) -> None:
        self._nav_menu.set_active_route(route)
