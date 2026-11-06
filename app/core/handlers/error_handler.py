import asyncio
import sys
import traceback

from types import TracebackType
from typing import Any

import httpx

from PySide6.QtCore import QObject, Signal, Slot, Qt
from PySide6.QtWidgets import QApplication, QMessageBox


class ErrorHandler(QObject):
    _error_occurred = Signal(str, str)

    def __init__(self) -> None:
        super().__init__()

        self._error_occurred.connect(
            self._show_error,
            Qt.ConnectionType.QueuedConnection,
        )

    def _log_error(
        self,
        title: str,
        message: str,
    ) -> None:
        print(
            f"\n{'=' * 80}\n" f"{title}\n" f"{'=' * 80}\n" f"{message}\n",
            file=sys.stderr,
            flush=True,
        )

    def show_error(
        self,
        message: str,
        title: str = "Ошибка",
    ) -> None:
        self._log_error(title, message)
        self._error_occurred.emit(title, message)

    def handle_exception(
        self,
        exc_type: type[BaseException],
        exc_value: BaseException,
        exc_traceback: TracebackType | None,
    ) -> None:
        traceback.print_exception(
            exc_type,
            exc_value,
            exc_traceback,
        )

        self.handle_error(
            exc_value,
            "Непредвиденная ошибка",
        )

    def handle_error(
        self,
        exception: BaseException,
        title: str = "Ошибка",
    ) -> None:
        traceback_text = "".join(
            traceback.format_exception(
                type(exception),
                exception,
                exception.__traceback__,
            )
        )

        if isinstance(exception, httpx.HTTPStatusError):
            response = exception.response

            try:
                data = response.json()
                detail = data.get("detail", response.text)
            except (ValueError, AttributeError):
                detail = response.text

            message = (
                f"{detail}\n\n"
                f"HTTP-статус: {response.status_code}\n"
                f"Метод: {response.request.method}\n"
                f"URL: {response.request.url}"
            )
        else:
            message = f"{type(exception).__name__}: {exception}"

        full_message = f"{message}\n\n" f"Подробности:\n" f"{traceback_text}"

        self.show_error(full_message, title)

    @Slot(str, str)
    def _show_error(
        self,
        title: str,
        message: str,
    ) -> None:
        if QApplication.instance() is None:
            return

        QMessageBox.critical(None, title, message)


error_handler: ErrorHandler | None = None


def setup_exception_handler() -> None:
    global error_handler

    error_handler = ErrorHandler()
    sys.excepthook = error_handler.handle_exception


def setup_asyncio_exception_handler(
    loop: asyncio.AbstractEventLoop,
) -> None:
    loop.set_exception_handler(handle_asyncio_exception)


def handle_asyncio_exception(
    loop: asyncio.AbstractEventLoop,
    context: dict[str, Any],
) -> None:
    exception = context.get("exception")

    if isinstance(exception, BaseException):
        assert error_handler is not None

        error_handler.handle_exception(
            type(exception),
            exception,
            exception.__traceback__,
        )
    else:
        message = context.get(
            "message",
            "Неизвестная ошибка асинхронной операции",
        )

        assert error_handler is not None
        error_handler.show_error(
            str(message),
            "Ошибка асинхронной операции",
        )


def show_error(
    message: str,
    title: str = "Ошибка",
) -> None:
    if error_handler is not None:
        error_handler.show_error(message, title)


def handle_error(
    exception: Exception,
    title: str = "Ошибка",
) -> None:
    if error_handler is not None:
        error_handler.handle_error(exception, title)
