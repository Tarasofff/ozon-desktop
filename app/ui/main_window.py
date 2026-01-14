from PySide6.QtWidgets import QMainWindow, QStackedWidget
from ui.patients_view import PatientsView
from core import app_config
from core.constants import AppRoutes
from infrastructure.router.router import Router
from .start_view import StartView
from .login_view import LoginView
from .register_view import RegisterView
from PySide6.QtGui import QIcon


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
        self.patients = PatientsView()

        self.router.register(AppRoutes.START, self.start)
        self.router.register(AppRoutes.LOGIN, self.login)
        self.router.register(AppRoutes.REGISTRATION, self.register)
        self.router.register(AppRoutes.PATIENTS, self.patients)

        self.router.navigate(AppRoutes.START)

    def _setup_router(self) -> None:
        self.router = Router(self.stack)

    def _setup_navigation(self) -> None:
        self.router.route_changed.connect(self._on_route_changed)

        self.start.vm.show_login.connect(lambda: self.router.navigate(AppRoutes.LOGIN))
        self.start.vm.show_register.connect(
            lambda: self.router.navigate(AppRoutes.REGISTRATION)
        )

        self.login.back_button.back_clicked.connect(
            lambda: self.router.navigate(AppRoutes.START)
        )
        self.register.back_button.back_clicked.connect(
            lambda: self.router.navigate(AppRoutes.START)
        )

        self.login.vm.success.connect(lambda: self._on_login_success())
        self.register.vm.success.connect(lambda: self._on_login_success())

        self.login.vm.success.connect(lambda: self.router.navigate(AppRoutes.PATIENTS))
        self.register.vm.success.connect(
            lambda: self.router.navigate(AppRoutes.PATIENTS)
        )

    def _on_route_changed(self, route: str) -> None:
        if route == AppRoutes.REGISTRATION:
            self.register.vm.load_roles()

    def _on_login_success(self):
        self.patients.load_patients()
        self.router.navigate(AppRoutes.PATIENTS)
