from core.app_config import app_config


class BaseApi:
    _PREFIX = f"{app_config.api_url}/v1"

    def _pagination(self, limit: int, offset: int) -> str:
        return f"limit={limit}&offset={offset}"


class UserApi(BaseApi):

    def __init__(self):
        self.INDEX = f"{self._PREFIX}/user"
        self.LOGIN = f"{self.INDEX}/login"
        self.REGISTRATION = f"{self.INDEX}/register"

    def get_all_roles(self, limit: int, offset: int) -> str:
        return f"{self.INDEX}/role?{self._pagination(limit, offset)}"


class PatientApi(BaseApi):

    def __init__(self):
        self.INDEX = f"{self._PREFIX}/patient"
        self.CREATE = f"{self.INDEX}/create"

    def get_by_id(self, patient_id: int) -> str:
        return f"{self.INDEX}/detail/id/{patient_id}"

    def update_by_id(self, patient_id: int) -> str:
        return f"{self.INDEX}/update/id/{patient_id}"

    def filter_by_fields(self, limit: int, offset: int) -> str:
        return f"{self.INDEX}/filter?{self._pagination(limit, offset)}"


class DoctorApi(BaseApi):

    def __init__(self):
        self.INDEX = f"{self._PREFIX}/doctor"

    def get_all(self, limit: int, offset: int) -> str:
        return f"{self.INDEX}?{self._pagination(limit, offset)}"

    def get_all_specializations(self, limit: int, offset: int) -> str:
        return f"{self.INDEX}/specialization?{self._pagination(limit, offset)}"


class DiagnoseApi(BaseApi):

    def __init__(self):
        self.INDEX = f"{self._PREFIX}/diagnose"

    def get_all(self, limit: int, offset: int) -> str:
        return f"{self.INDEX}?{self._pagination(limit, offset)}"


user_api = UserApi()
patient_api = PatientApi()
doctor_api = DoctorApi()
diagnose_api = DiagnoseApi()
