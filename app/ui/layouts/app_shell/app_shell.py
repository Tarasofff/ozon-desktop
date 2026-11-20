from enum import StrEnum
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from ui.layouts.app_shell.sidebar import Sidebar
from ui.layouts.app_shell.top_bar import TopBar


class AppShell(QWidget):
    navigation_requested = Signal(object)
    settings_requested = Signal()
    logout_requested = Signal()
    profile_requested = Signal()

    def __init__(
        self,
        nav_items: list[tuple[StrEnum, str]],
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)

        self._setup_ui()
        self._create_sidebar(nav_items)
        self._create_main_area()
        self._setup_signals()

    def _setup_ui(self) -> None:
        self.setObjectName("appShell")

        self._root_layout = QHBoxLayout(self)
        self._root_layout.setContentsMargins(0, 0, 0, 0)
        self._root_layout.setSpacing(0)

    def _create_sidebar(
        self,
        nav_items: list[tuple[StrEnum, str]],
    ) -> None:
        self._sidebar = Sidebar(nav_items)
        self._root_layout.addWidget(self._sidebar)

    def _create_main_area(self) -> None:
        self._main_area = QWidget()
        self._main_area.setObjectName("mainArea")

        layout = QVBoxLayout(self._main_area)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self._top_bar = TopBar()
        layout.addWidget(self._top_bar)

        self.content_stack = QStackedWidget()
        self.content_stack.setObjectName("contentStack")
        layout.addWidget(self.content_stack)

        self._root_layout.addWidget(self._main_area)

    def _setup_signals(self) -> None:
        self._sidebar.navigation_requested.connect(self.navigation_requested.emit)

        self._sidebar.settings_requested.connect(self.settings_requested.emit)

        self._sidebar.logout_requested.connect(self.logout_requested.emit)

        self._top_bar.profile_requested.connect(self.profile_requested.emit)

    def set_page_title(self, title: str) -> None:
        self._top_bar.set_page_title(title)

    def set_active_navigation(self, route: StrEnum) -> None:
        self._sidebar.set_active_route(route)
