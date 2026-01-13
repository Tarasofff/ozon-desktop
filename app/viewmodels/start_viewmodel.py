from PySide6.QtCore import Signal
from .base_viewmodel import BaseViewModel


class StartViewModel(BaseViewModel):
    show_login = Signal()
    show_register = Signal()
