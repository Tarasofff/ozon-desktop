from PySide6.QtWidgets import QMainWindow, QStackedWidget
from infrastructure.navigation.page_config import APP_PAGES
from ui.layouts.app_shell.app_shell import AppShell
from infrastructure.navigation.routes import AppRoutes, AuthRoutes
from ui.views.patients.patients_view import PatientsView
from ui.views.auth.register_view import RegisterView
from core import app_config
from infrastructure.navigation.router import Router
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTimer
from ui.views.auth.start_view import StartView
from ui.views.auth.login_view import LoginView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._setup_window()
        self._setup_stack()
        self._setup_router()
        self._setup_views()
        self._setup_navigation()

        # TEST
        QTimer.singleShot(0, self._on_login_success)

    def _setup_window(self) -> None:
        self.setWindowTitle(app_config.app_name)
        self.resize(1000, 700)
        self.setMinimumSize(900, 600)
        self.setWindowIcon(QIcon("assets/icons/main.png"))

    def _setup_stack(self) -> None:
        # Главный стек: авторизация / рабочее пространство
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Стек авторизации
        self.auth_stack = QStackedWidget()
        self.stack.addWidget(self.auth_stack)

        # Основная оболочка приложения
        self.app_shell = AppShell(
            nav_items=[
                (page.route, page.navigation_title) for page in APP_PAGES.values()
            ]
        )
        self.stack.addWidget(self.app_shell)

    def _setup_views(self) -> None:
        self.start = StartView()
        self.login = LoginView()
        self.register = RegisterView()
        self.patients = PatientsView()

        self.auth_router.register(AuthRoutes.START, self.start)
        self.auth_router.register(AuthRoutes.LOGIN, self.login)
        self.auth_router.register(AuthRoutes.REGISTRATION, self.register)

        self.app_router.register(AppRoutes.PATIENTS, self.patients)

        self.auth_router.navigate(AuthRoutes.START)

    def _setup_router(self) -> None:
        self.auth_router: Router[AuthRoutes] = Router(self.auth_stack)
        self.app_router: Router[AppRoutes] = Router(self.app_shell.content_stack)

    def _setup_navigation(self) -> None:
        self.start.vm.show_login.connect(
            lambda: self.auth_router.navigate(AuthRoutes.LOGIN)
        )
        self.start.vm.show_register.connect(
            lambda: self.auth_router.navigate(AuthRoutes.REGISTRATION)
        )

        self.login.back_button.btn_clicked.connect(
            lambda: self.auth_router.navigate(AuthRoutes.START)
        )
        self.register.back_button.btn_clicked.connect(
            lambda: self.auth_router.navigate(AuthRoutes.START)
        )

        self.login.vm.success.connect(self._on_login_success)
        self.register.vm.success.connect(self._on_login_success)

        self.app_shell.navigation_requested.connect(self.app_router.navigate)

        self.app_router.route_changed.connect(self._on_app_route_changed)

    def _on_login_success(self):
        self.stack.setCurrentWidget(self.app_shell)
        self.app_router.navigate(AppRoutes.PATIENTS)
        self.patients.vm.load_patients()

    def _on_app_route_changed(self, route: AppRoutes) -> None:
        page = APP_PAGES.get(route)

        title = page.page_title if page else app_config.app_name

        self.app_shell.set_page_title(title)
        self.app_shell.set_active_navigation(route)
