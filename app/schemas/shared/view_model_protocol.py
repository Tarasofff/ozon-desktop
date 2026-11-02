from typing import Protocol
from PySide6.QtCore import SignalInstance


class ViewModelProtocol(Protocol):
    success: SignalInstance
    error: SignalInstance
