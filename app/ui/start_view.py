from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt
from viewmodels.start_viewmodel import StartViewModel

class StartView(QWidget):
    def __init__(self):
        super().__init__()
        self.vm = StartViewModel()

        self._create_widgets()
        self._setup_layout()
        self._connect_signals()

    def _create_widgets(self):
        self.title_label = QLabel("Добро пожаловать")
        self.title_label.setObjectName("title")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.login_button = QPushButton("Вход")
        self.register_button = QPushButton("Регистрация")

    def _setup_layout(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)

        layout.addWidget(self.title_label)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

    def _connect_signals(self):
        self.login_button.clicked.connect(self.vm.show_login)
        self.register_button.clicked.connect(self.vm.show_register)
