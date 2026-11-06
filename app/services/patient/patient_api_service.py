from infrastructure.api.http_client import http_client
from schemas.patient import PaginatedPatientsResponse
from infrastructure.api.routes import patient_api


class PatientApiService:
    def __init__(self):
        pass

    async def get_patients(self, limit: int, offset: int) -> PaginatedPatientsResponse:
        response = await http_client.get(patient_api.get_list(limit, offset))
        response.raise_for_status()

        return PaginatedPatientsResponse.model_validate(response.json())
