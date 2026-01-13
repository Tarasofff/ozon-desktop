from PySide6.QtCore import QObject, Signal

class BaseViewModel(QObject):
    _success = Signal()
    _error = Signal(str)

    def emit_success(self):
        self._success.emit()

    def emit_error(self, msg: str):
        self._error.emit(msg)

    @property
    def success(self):
        return self._success

    @property
    def error(self):
        return self._error
