from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt
from viewmodels import StartViewModel


class StartView(QWidget):
    def __init__(self):
        super().__init__()
        self.vm = StartViewModel()

        self._create_widgets()
        self._setup_layout()
        self._connect_signals()

    def _create_widgets(self):
        self._title_label = QLabel("Добро пожаловать")
        self._title_label.setObjectName("title")
        self._title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._login_button = QPushButton("Вход")
        self._register_button = QPushButton("Регистрация")

    def _setup_layout(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)

        layout.addWidget(self._title_label)
        layout.addWidget(self._login_button)
        layout.addWidget(self._register_button)

    def _connect_signals(self):
        self._login_button.clicked.connect(self.vm.show_login)
        self._register_button.clicked.connect(self.vm.show_register)
