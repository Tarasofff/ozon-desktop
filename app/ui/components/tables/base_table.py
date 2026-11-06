from ui.components.tables.table_column import TableColumn
from typing import Any, Sequence
from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    QPersistentModelIndex,
    Qt,
)


class BaseTable(QAbstractTableModel):

    def __init__(
        self,
        columns: Sequence[TableColumn],
        data: Sequence[Any] | None = None,
    ) -> None:
        super().__init__()

        self._columns = list(columns)
        self._data = list(data) if data is not None else []

    def rowCount(
        self,
        parent: QModelIndex | QPersistentModelIndex = QModelIndex(),
    ) -> int:
        if parent.isValid():
            return 0

        return len(self._data)

    def columnCount(
        self,
        parent: QModelIndex | QPersistentModelIndex = QModelIndex(),
    ) -> int:
        if parent.isValid():
            return 0

        return len(self._columns)

    def data(
        self,
        index: QModelIndex | QPersistentModelIndex,
        role: int = Qt.ItemDataRole.DisplayRole,
    ) -> Any:
        if not index.isValid():
            return None

        if not (
            0 <= index.row() < len(self._data)
            and 0 <= index.column() < len(self._columns)
        ):
            return None

        item = self._data[index.row()]
        column = self._columns[index.column()]

        if role == Qt.ItemDataRole.DisplayRole:
            value = column.getter(item)
            return value if value is not None else "—"

        if role == Qt.ItemDataRole.TextAlignmentRole:
            return column.align

        if role == Qt.ItemDataRole.UserRole:
            return item

        return None

    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int = Qt.ItemDataRole.DisplayRole,
    ) -> Any:
        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            if 0 <= section < len(self._columns):
                return self._columns[section].title

        return None

    def set_data(self, data: Sequence[Any]) -> None:
        self.beginResetModel()
        self._data = list(data)
        self.endResetModel()

    def get_row(self, row: int) -> Any | None:
        if 0 <= row < len(self._data):
            return self._data[row]
        return None
