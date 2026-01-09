from PySide6.QtCore import QObject, Signal


class StartViewModel(QObject):
    show_login = Signal()
    show_register = Signal()
