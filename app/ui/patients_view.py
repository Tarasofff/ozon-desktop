from models.patient_model import PatientModel
from ui.components import TableColumn, BaseTable
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableView, QPushButton
from PySide6.QtCore import Qt


class PatientsView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пациенты")
        self.resize(900, 500)

        self._create_widgets()
        self._setup_layout()
        self._connect_signals()

    def _create_widgets(self):
        self.title_label = QLabel("Пациенты")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setObjectName("title")

        self.refresh_button = QPushButton("Обновить список")

        self.columns = [
            TableColumn("Имя", lambda p: p.first_name),
            TableColumn("Фамилия", lambda p: p.last_name),
            TableColumn("Отчество", lambda p: p.middle_name),
            TableColumn(
                "Телефон", lambda p: p.phone, align=Qt.AlignmentFlag.AlignCenter
            ),
            TableColumn(
                "Дата рождения",
                lambda p: (p.date_of_birth),
                align=Qt.AlignmentFlag.AlignCenter,
            ),
            TableColumn("Email", lambda p: p.email or "—"),
            TableColumn(
                "Активен",
                lambda p: "Да" if p.is_active else "Нет",
                align=Qt.AlignmentFlag.AlignCenter,
            ),
            TableColumn("Заметки", lambda p: p.notes or "—"),
        ]

        self.table_view = QTableView()
        self.model = BaseTable(columns=self.columns, data=[])
        self.table_view.setModel(self.model)

        self.table_view.horizontalHeader().setStretchLastSection(True)
        self.table_view.verticalHeader().setVisible(False)
        self.table_view.setAlternatingRowColors(True)
        self.table_view.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.table_view.setSelectionMode(QTableView.SelectionMode.SingleSelection)

    def _setup_layout(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.title_label)
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.table_view)

    def _connect_signals(self):
        self.refresh_button.clicked.connect(self.load_patients)

    def set_patients(self, patients: list[PatientModel]):
        self.model.set_data(patients)

    def load_patients(self):
        example_patients = [
            PatientModel(
                first_name="Иван",
                middle_name="Иванович",
                last_name="Иванов",
                phone="123456789",
                date_of_birth="2000.03.13",
                email="ivan@mail.com",
                is_active=True,
                notes="Нужно проверить",
            ),
            PatientModel(
                first_name="Мария",
                middle_name="Сергеевна",
                last_name="Петрова",
                phone="987654321",
                date_of_birth="2000.03.13",
                email=None,
                is_active=False,
                notes=None,
            ),
        ]
        self.set_patients(example_patients)
