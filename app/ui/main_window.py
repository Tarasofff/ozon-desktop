from PySide6.QtWidgets import QMainWindow, QStackedWidget
from core.app_routes import app_routes
from infrastructure.router.router import Router
from ui.start_view import StartView
from ui.login_view import LoginView
from ui.register_view import RegisterView
from PySide6.QtGui import QIcon
from core.app_config import app_config


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._setup_window()
        self._setup_stack()
        self._setup_router()
        self._setup_views()
        self._setup_navigation()

    def _setup_window(self) -> None:
        self.setWindowTitle(app_config.app_name)
        self.resize(1000, 700)
        self.setMinimumSize(900, 600)
        self.setWindowIcon(QIcon("assets/icons/main.png"))

    def _setup_stack(self) -> None:
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

    def _setup_views(self) -> None:
        self.start = StartView()
        self.login = LoginView()
        self.register = RegisterView()

        self.router.register(app_routes.START, self.start)
        self.router.register(app_routes.LOGIN, self.login)
        self.router.register(app_routes.REGISTRATION, self.register)

        self.router.navigate(app_routes.START)

    def _setup_router(self) -> None:
        self.router = Router(self.stack)

    def _setup_navigation(self) -> None:
        self.router.route_changed.connect(self._on_route_changed)

        self.start.vm.show_login.connect(lambda: self.router.navigate(app_routes.LOGIN))
        self.start.vm.show_register.connect(
            lambda: self.router.navigate(app_routes.REGISTRATION)
        )

        self.login.back_button.back_clicked.connect(
            lambda: self.router.navigate(app_routes.START)
        )
        self.register.back_button.back_clicked.connect(
            lambda: self.router.navigate(app_routes.START)
        )

    def _on_route_changed(self, route: str) -> None:
        if route == app_routes.REGISTRATION:
            self.register.vm.load_roles()
