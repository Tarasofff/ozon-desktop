from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QButtonGroup,
    QFrame,
    QHBoxLayout,
    QLabel,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)
from enum import StrEnum
from ui.components.buttons.base_button import BaseButton


class AppShell(QWidget):
    navigation_requested = Signal(object)
    settings_requested = Signal()
    logout_requested = Signal()
    profile_requested = Signal()

    SIDEBAR_WIDTH = 240
    TOPBAR_HEIGHT = 72

    def __init__(
        self,
        nav_items: list[tuple[StrEnum, str]],
        parent: QWidget | None = None,
    ):
        super().__init__(parent)

        self._nav_items = nav_items
        self._nav_buttons: dict[StrEnum, BaseButton] = {}

        self._setup_ui()
        self._create_sidebar()
        self._create_main_area()

    def _setup_ui(self) -> None:
        self.setObjectName("appShell")

        self._root_layout = QHBoxLayout(self)
        self._root_layout.setContentsMargins(0, 0, 0, 0)
        self._root_layout.setSpacing(0)

    def _create_sidebar(self) -> None:
        self._sidebar = QFrame()
        self._sidebar.setObjectName("sidebar")
        self._sidebar.setFixedWidth(self.SIDEBAR_WIDTH)

        layout = QVBoxLayout(self._sidebar)
        layout.setContentsMargins(16, 24, 16, 20)
        layout.setSpacing(8)

        # Logo
        self._logo_label = QLabel("OZON DESKTOP")
        self._logo_label.setObjectName("brandLabel")
        layout.addWidget(self._logo_label)

        layout.addSpacing(28)

        # Navigation
        self._navigation_group = QButtonGroup(self)
        self._navigation_group.setExclusive(True)

        for route, title in self._nav_items:
            button = BaseButton(title)
            button.setObjectName("navButton")
            button.setCheckable(True)
            button.setCursor(Qt.CursorShape.PointingHandCursor)

            button.btn_clicked.connect(
                lambda checked=False, route=route: self.navigation_requested.emit(route)
            )

            self._navigation_group.addButton(button)
            self._nav_buttons[route] = button
            layout.addWidget(button)

        layout.addStretch()

        # Settings
        self._settings_button = BaseButton("Настройки")
        self._settings_button.setObjectName("navButton")
        self._settings_button.setCursor(Qt.CursorShape.PointingHandCursor)
        layout.addWidget(self._settings_button)
        self._settings_button.clicked.connect(self.settings_requested.emit)

        self._logout_button = BaseButton("Выйти")
        self._logout_button.setObjectName("logoutButton")
        self._logout_button.setCursor(Qt.CursorShape.PointingHandCursor)
        layout.addWidget(self._logout_button)
        self._logout_button.clicked.connect(self.logout_requested.emit)

        self._root_layout.addWidget(self._sidebar)

    def _create_main_area(self) -> None:
        self._main_area = QWidget()
        self._main_area.setObjectName("mainArea")

        layout = QVBoxLayout(self._main_area)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Top bar
        self._top_bar = QFrame()
        self._top_bar.setObjectName("topBar")
        self._top_bar.setFixedHeight(self.TOPBAR_HEIGHT)

        top_layout = QHBoxLayout(self._top_bar)
        top_layout.setContentsMargins(28, 0, 28, 0)

        self._page_title = QLabel("Главная")
        self._page_title.setObjectName("pageTitle")

        top_layout.addWidget(self._page_title)
        top_layout.addStretch()

        self._profile_button = BaseButton("Мой профиль  ▾")
        self._profile_button.setObjectName("profileButton")
        self._profile_button.setCursor(Qt.CursorShape.PointingHandCursor)

        top_layout.addWidget(self._profile_button)

        self._profile_button.clicked.connect(self.profile_requested.emit)

        layout.addWidget(self._top_bar)

        # Page content
        self.content_stack = QStackedWidget()
        self.content_stack.setObjectName("contentStack")

        layout.addWidget(self.content_stack)

        self._root_layout.addWidget(self._main_area)

    def set_page_title(self, title: str) -> None:
        self._page_title.setText(title)

    def set_active_navigation(self, route: StrEnum) -> None:
        button = self._nav_buttons.get(route)

        if button is not None:
            button.setChecked(True)
