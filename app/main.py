import sys, asyncio
from PySide6.QtWidgets import QApplication
from qasync import QEventLoop
from pathlib import Path
from core.config.app_config import app_config
from core.handlers.global_exception_handler import setup_exception_handler
from main_window import MainWindow


def load_styles(app: QApplication):
    styles_dir = Path(__file__).parent / "styles"
    qss = ""

    for file in styles_dir.glob("*.qss"):
        qss += file.read_text(encoding="utf-8")

    app.setStyleSheet(qss)


def main():
    app = QApplication(sys.argv)
    app.setApplicationName(app_config.app_name)
    app.setOrganizationName(app_config.app_name)

    setup_exception_handler()

    load_styles(app)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = MainWindow()
    window.show()

    with loop:
        loop.run_forever()


if __name__ == "__main__":
    main()
