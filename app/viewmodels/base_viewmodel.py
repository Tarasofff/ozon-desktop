from typing import Any, Awaitable, Callable, Optional
from PySide6.QtCore import QObject, Signal
import asyncio

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

    async def _async_api_request_task(
        self,
        request_func: Callable[..., Awaitable[tuple[bool, Any]]],
        *args: Any,
        success_callback: Optional[Callable[[Any], None]],
        error_prefix: str,
    ):
        """
        Универсальный обработчик асинхронных задач.

        request_func: async функция, возвращающая (ok: bool, data)
        args: аргументы для request_func
        success_callback: функция, вызываемая с data при успехе
        error_prefix: текст для ошибки
        success_msg: текст для успешной операции
        """
        try:
            ok, data = await request_func(*args)
            if ok:
                if success_callback:
                    if asyncio.iscoroutinefunction(success_callback):
                        await success_callback(data)
                    else:
                        success_callback(data)
                    self.emit_success()
            else:
                self.emit_error(f"{error_prefix}: {data}")
        except Exception as e:
            self.emit_error(f"{error_prefix}: {str(e)}")

    def _run_async_task(
        self,
        request_func: Callable[..., Awaitable[tuple[bool, Any]]],
        *args: Any,
        success_callback: Optional[Callable[[Any], None]] = None,
        error_prefix: str = "Ошибка",
    ):
        """
        Синхронная обёртка для запуска асинхронной задачи через asyncio.create_task.
        """
        asyncio.create_task(
            self._async_api_request_task(
                request_func,
                *args,
                success_callback=success_callback,
                error_prefix=error_prefix,
            )
        )
