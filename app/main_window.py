from PySide6.QtWidgets import QMainWindow, QStackedWidget
from infrastructure.navigation.routes import AppRoutes
from ui.views.patients.patients_view import PatientsView
from ui.views.registration.register_view import RegisterView
from core import app_config
from infrastructure.navigation.router import Router
from PySide6.QtGui import QIcon
from ui.views.start.start_view import StartView
from ui.views.login.login_view import LoginView


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
        self.start.vm.show_login.connect(lambda: self.router.navigate(AppRoutes.LOGIN))
        self.start.vm.show_register.connect(
            lambda: self.router.navigate(AppRoutes.REGISTRATION)
        )

        self.login.back_button.btn_clicked.connect(
            lambda: self.router.navigate(AppRoutes.START)
        )
        self.register.back_button.btn_clicked.connect(
            lambda: self.router.navigate(AppRoutes.START)
        )

        self.login.vm.success.connect(self._on_login_success)
        self.register.vm.success.connect(self._on_login_success)

    def _on_login_success(self):
        # self.patients.vm.load_patients()
        # self.router.navigate(AppRoutes.PATIENTS)
        pass
