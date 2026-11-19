from schemas.auth import AuthPayload
from ui.components.buttons.base_button import BaseButton
from ui.components.inputs.password_input import PasswordInput
from ui.components.inputs.phone_input import PhoneInput
from ui.views.base.form_container_view import FormContainerView
from viewmodels import LoginViewModel


class LoginView(FormContainerView):
    def __init__(self):
        super().__init__("Вход")

        self.vm = LoginViewModel()

        self._create_widgets()
        self._setup_layout()
        self._connect_signals()

    def _create_widgets(self):
        self._phone_input = PhoneInput()
        self._password_input = PasswordInput()
        self._login_button = BaseButton("Войти")

    def _setup_layout(self):
        self.add(self._phone_input)
        self.add(self._password_input)
        self.add(self._login_button)

    def _connect_signals(self):
        self._login_button.clicked.connect(self._handle_login)

    def _get_validated_auth_payload(self) -> AuthPayload | None:
        if not self._phone_input.validate() or not self._password_input.validate():
            return None

        return AuthPayload(
            phone=self._phone_input.normalized_value(),
            password=self._password_input.value(),
        )

    def _handle_login(self):
        auth_payload = self._get_validated_auth_payload()

        if auth_payload is None:
            return

        self.vm.login(
            AuthPayload(phone=auth_payload.phone, password=auth_payload.password)
        )
