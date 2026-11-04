from typing import Any, Awaitable, Callable, TypeVar
from PySide6.QtCore import QObject, Signal
import asyncio
import inspect
from core.handlers.error_handler import handle_error

T = TypeVar("T")


class BaseViewModel(QObject):
    _success = Signal()
    _error = Signal(str)

    def emit_success(self) -> None:
        self._success.emit()

    def emit_error(self, msg: str) -> None:
        self._error.emit(msg)

    @property
    def success(self):
        return self._success

    @property
    def error(self):
        return self._error

    async def _handle_request(
        self,
        request_func: Callable[..., Awaitable[T]],
        *args: Any,
        success_callback: Callable[[T], None | Awaitable[None]] | None = None,
        error_prefix: str = "Ошибка",
    ) -> None:
        try:
            result = await request_func(*args)

            if success_callback is not None:
                callback_result = success_callback(result)

                if inspect.isawaitable(callback_result):
                    await callback_result

            self.emit_success()

        except asyncio.CancelledError:
            raise

        except Exception as e:
            self.emit_error(f"{error_prefix}: {e}")
            handle_error(e, error_prefix)

    def run_async_task(
        self,
        request_func: Callable[..., Awaitable[T]],
        *args: Any,
        success_callback: Callable[[T], None | Awaitable[None]] | None = None,
        error_prefix: str = "Ошибка",
    ) -> asyncio.Task[None]:
        return asyncio.create_task(
            self._handle_request(
                request_func,
                *args,
                success_callback=success_callback,
                error_prefix=error_prefix,
            )
        )
