from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QStackedWidget, QWidget


class Router(QObject):
    route_changed = Signal(str)

    def __init__(self, stack: QStackedWidget):
        super().__init__()
        self._stack = stack
        self._routes: dict[str, QWidget] = {}
        self._current_route: str | None = None

    def register(self, name: str, widget: QWidget) -> None:
        if name in self._routes:
            raise ValueError(f"Route '{name}' already registered")

        self._routes[name] = widget
        self._stack.addWidget(widget)

    def navigate(self, name: str) -> None:
        if name not in self._routes:
            raise KeyError(f"Route '{name}' not found")

        self._current_route = name
        self._stack.setCurrentWidget(self._routes[name])
        self.route_changed.emit(name)

    @property
    def current_route(self) -> str | None:
        return self._current_route
