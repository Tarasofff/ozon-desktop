from models.doctor_model import PaginatedDoctorSpecializationModel
from core.constants import doctor_api
from infrastructure.http.client import http


class DoctorApiService:

    async def get_all_specializations_request(
        self, limit: int, offset: int
    ) -> tuple[bool, PaginatedDoctorSpecializationModel]:
        response = await http.get(
            doctor_api.get_all_specializations(limit, offset),
        )

        return response.status_code == 200, response.json()
