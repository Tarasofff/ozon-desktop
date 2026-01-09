from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal


class BackButton(QPushButton):
    back_clicked = Signal()

    def __init__(self):
        super().__init__("← Назад")
        self.setObjectName("back")
        self.clicked.connect(self.back_clicked)
    