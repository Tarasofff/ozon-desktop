from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, QPersistentModelIndex
from typing import List, Any
from ui.components.tables.table_column import TableColumn


class BaseTable(QAbstractTableModel):
    def __init__(self, columns: List[TableColumn], data: List[Any] | None = None):
        super().__init__()
        self._columns = columns
        self._data = data or []

    def rowCount(
        self,
        parent: QModelIndex | QPersistentModelIndex = QModelIndex(),
    ) -> int:
        return len(self._data)

    def columnCount(
        self, parent: QModelIndex | QPersistentModelIndex = QModelIndex()
    ) -> int:
        return len(self._columns)

    def data(
        self,
        index: QModelIndex | QPersistentModelIndex,
        role: int = Qt.ItemDataRole.DisplayRole,
    ):
        if not index.isValid():
            return None

        item = self._data[index.row()]
        column = self._columns[index.column()]

        if role == Qt.ItemDataRole.DisplayRole:
            value = column.getter(item)
            return value if value is not None else "—"

        if role == Qt.ItemDataRole.TextAlignmentRole:
            return column.align

        return None

    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int = Qt.ItemDataRole.DisplayRole,
    ):
        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole
        ):
            return self._columns[section].title
        return None

    def set_data(self, data: List[Any]):
        self.beginResetModel()
        self._data = data
        self.endResetModel()

    def get_row(self, row: int):
        return self._data[row]
