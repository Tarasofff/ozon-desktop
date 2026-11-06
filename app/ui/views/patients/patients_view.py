from app.schemas.patient import PaginatedPatientsResponse
from viewmodels.patients_viewmodel import PatientsViewModel
from ui.components import TableColumn, BaseTable
from PySide6.QtWidgets import (
    QAbstractItemView,
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableView,
    QPushButton,
)
from PySide6.QtCore import QTimer, Qt, Slot
from schemas import PatientBase


class PatientsView(QWidget):
    def __init__(self):
        super().__init__()

        self.vm = PatientsViewModel()

        self._create_widgets()
        self._setup_layout()
        self._connect_signals()

        QTimer.singleShot(0, self.vm.load_patients)

    def _create_widgets(self) -> None:
        self._title_label = QLabel("Пациенты")
        self._title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._title_label.setObjectName("title")

        self._refresh_button = QPushButton("Обновить список")

        columns = [
            TableColumn(
                "Имя",
                lambda p: p.first_name,
            ),
            TableColumn(
                "Фамилия",
                lambda p: p.last_name,
            ),
            TableColumn(
                "Отчество",
                lambda p: p.patronymic,
            ),
            TableColumn(
                "Телефон",
                lambda p: p.phone,
                align=Qt.AlignmentFlag.AlignCenter,
            ),
            TableColumn(
                "Дата рождения",
                lambda p: p.date_of_birth.strftime("%d.%m.%Y"),
                align=Qt.AlignmentFlag.AlignCenter,
            ),
            TableColumn(
                "Email",
                lambda p: p.email,
            ),
            TableColumn(
                "Активен",
                lambda p: "Да" if p.is_active else "Нет",
                align=Qt.AlignmentFlag.AlignCenter,
            ),
        ]

        self._table_model = BaseTable(
            columns=columns,
            data=[],
        )

        self._table_view = QTableView()
        self._table_view.setModel(self._table_model)

        self._table_view.horizontalHeader().setStretchLastSection(True)
        self._table_view.verticalHeader().setVisible(False)

        self._table_view.setAlternatingRowColors(True)

        self._table_view.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        self._table_view.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        self._table_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

    def _setup_layout(self):
        self.setWindowTitle("Пациенты")
        self.resize(900, 500)

        layout = QVBoxLayout(self)
        layout.addWidget(self._title_label)
        layout.addWidget(self._refresh_button)
        layout.addWidget(self._table_view)

    def _connect_signals(self) -> None:
        self._refresh_button.clicked.connect(self._on_refresh_clicked)

        self.vm.patients_loaded.connect(self._on_patients_loaded)

    def set_patients(self, patients: list[PatientBase]):
        self._table_model.set_data(patients)

    @Slot(bool)
    def _on_refresh_clicked(self, checked: bool = False) -> None:
        self.vm.load_patients()

    @Slot(object)
    def _on_patients_loaded(
        self,
        response: PaginatedPatientsResponse,
    ) -> None:
        self._table_model.set_data(response.data)
        self._table_view.resizeColumnsToContents()
