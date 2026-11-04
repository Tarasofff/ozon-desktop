import sys
import traceback
from types import TracebackType

from PySide6.QtWidgets import QApplication, QMessageBox


def handle_exception(
    exc_type: type[BaseException],
    exc_value: BaseException,
    exc_traceback: TracebackType | None,
) -> None:
    traceback.print_exception(exc_type, exc_value, exc_traceback)

    app = QApplication.instance()

    if app is not None:
        QMessageBox.critical(
            None,
            "Непредвиденная ошибка",
            (
                "Произошла непредвиденная ошибка:\n\n"
                f"{exc_type.__name__}: {exc_value}\n\n"
                "Подробности ошибки выведены в консоль."
            ),
        )


def setup_exception_handler() -> None:
    sys.excepthook = handle_exception
