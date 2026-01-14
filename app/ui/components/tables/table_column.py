from dataclasses import dataclass
from typing import Callable, Any
from PySide6.QtCore import Qt


@dataclass
class TableColumn:
    title: str
    getter: Callable[[Any], Any]
    align: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignLeft
