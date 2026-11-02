from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal


class BaseButton(QPushButton):
    btn_clicked = Signal()

    def __init__(self, title: str):
        super().__init__(title)
        self.clicked.connect(self.btn_clicked)
