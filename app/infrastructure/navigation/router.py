from typing import Generic, TypeVar
from enum import StrEnum

from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QStackedWidget, QWidget

RouteT = TypeVar("RouteT", bound=StrEnum)


class Router(QObject, Generic[RouteT]):
    route_changed = Signal(object)

    def __init__(self, stack: QStackedWidget):
        super().__init__()

        self._stack = stack
        self._routes: dict[RouteT, QWidget] = {}
        self._current_route: RouteT | None = None

    def register(self, route: RouteT, widget: QWidget) -> None:
        if route in self._routes:
            raise ValueError(f"Route '{route}' already registered")

        self._routes[route] = widget
        self._stack.addWidget(widget)

    def navigate(self, route: RouteT) -> None:
        if route not in self._routes:
            raise KeyError(f"Route '{route}' not found")

        self._current_route = route
        self._stack.setCurrentWidget(self._routes[route])
        self.route_changed.emit(route)

    @property
    def current_route(self) -> RouteT | None:
        return self._current_route

    @property
    def registered_routes(self) -> tuple[RouteT, ...]:
        return tuple(self._routes.keys())
