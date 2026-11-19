import sys, asyncio
from PySide6.QtWidgets import QApplication
from qasync import QEventLoop
from pathlib import Path
from core.handlers.error_handler import (
    setup_asyncio_exception_handler,
    setup_exception_handler,
)
from app.ui.main_window import MainWindow


def load_styles(app: QApplication) -> None:
    styles_dir = Path(__file__).parent / "styles"

    qss = ""

    for file in sorted(styles_dir.glob("*.qss")):
        qss += file.read_text(encoding="utf-8")
        qss += "\n"

    app.setStyleSheet(qss)


def main():
    app = QApplication(sys.argv)

    setup_exception_handler()

    load_styles(app)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    setup_asyncio_exception_handler(loop)

    window = MainWindow()
    window.show()

    with loop:
        loop.run_forever()


if __name__ == "__main__":
    main()
