from PySide6.QtCore import Signal
from schemas.patient import PaginatedPatientsResponse
from viewmodels.base_viewmodel import BaseViewModel
from services.patient.patient_api_service import PatientApiService


class PatientsViewModel(BaseViewModel):
    _patients_loaded = Signal(object)

    def __init__(
        self,
    ) -> None:
        super().__init__()

        self._patient_api_service = PatientApiService()

        self._limit = 20
        self._offset = 0
        self._total = 0

    @property
    def patients_loaded(self):
        return self._patients_loaded

    @property
    def total(self) -> int:
        return self._total

    def _on_patients_loaded(
        self,
        response: PaginatedPatientsResponse,
    ) -> None:
        self._total = response.total
        self._limit = response.limit
        self._offset = response.offset

        self._patients_loaded.emit(response)

    def load_patients(
        self,
        limit: int | None = None,
        offset: int | None = None,
    ) -> None:
        if limit is not None:
            self._limit = limit

        if offset is not None:
            self._offset = offset

        self.run_async_task(
            self._patient_api_service.get_patients,
            self._limit,
            self._offset,
            success_callback=self._on_patients_loaded,
            error_prefix="Не удалось загрузить список пациентов",
        )
