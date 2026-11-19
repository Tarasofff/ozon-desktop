from enum import StrEnum

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QButtonGroup,
    QVBoxLayout,
    QWidget,
)

from ui.components.buttons.base_button import BaseButton


class NavMenu(QWidget):
    navigation_requested = Signal(object)

    def __init__(
        self,
        nav_items: list[tuple[StrEnum, str]],
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)

        self._nav_items = nav_items
        self._nav_buttons: dict[StrEnum, BaseButton] = {}

        self._setup_ui()
        self._create_buttons()

    def _setup_ui(self) -> None:
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(8)

        self._button_group = QButtonGroup(self)
        self._button_group.setExclusive(True)

    def _create_buttons(self) -> None:
        for route, title in self._nav_items:
            button = BaseButton(title)
            button.setObjectName("navButton")
            button.setCheckable(True)
            button.setCursor(Qt.CursorShape.PointingHandCursor)

            button.btn_clicked.connect(
                lambda route=route: self.navigation_requested.emit(route)
            )

            self._button_group.addButton(button)
            self._nav_buttons[route] = button

            self._layout.addWidget(button)

    def set_active_route(self, route: StrEnum) -> None:
        button = self._nav_buttons.get(route)

        if button is not None:
            button.setChecked(True)
