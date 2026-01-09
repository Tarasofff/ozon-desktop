from core.app_config import app_config


class BaseApi:
    _api_url = app_config.api_url

    PREFIX = f"{_api_url}/v1"


class UserApi(BaseApi):
    INDEX = f"{BaseApi.PREFIX}/user"

    login = f"{INDEX}/login"
    register = f"{INDEX}/register"

    @staticmethod
    def get_all_roles(limit: int, offset: int) -> str:
        return f"{UserApi.INDEX}/role?limit={limit}&offset={offset}"


class PatientApi(BaseApi):
    INDEX = f"{BaseApi.PREFIX}/patient"

    create = f"{INDEX}/create"
    # report = f"{INDEX}/report"  # TODO

    @staticmethod
    def get_by_id(patient_id: int) -> str:
        return f"{PatientApi.INDEX}/detail/id/{patient_id}"

    @staticmethod
    def update_by_id(patient_id: int) -> str:
        return f"{PatientApi.INDEX}/update/id/{patient_id}"

    @staticmethod
    def filter_by_fields(limit: int, offset: int) -> str:
        return f"{PatientApi.INDEX}/filter?limit={limit}&offset={offset}"


class DoctorApi(BaseApi):
    INDEX = f"{BaseApi.PREFIX}/doctor"

    @staticmethod
    def get_all(limit: int, offset: int) -> str:
        return f"{DoctorApi.INDEX}?limit={limit}&offset={offset}"

    @staticmethod
    def get_all_specializations(limit: int, offset: int) -> str:
        return f"{DoctorApi.INDEX}/specialization?limit={limit}&offset={offset}"


class DiagnoseApi(BaseApi):
    INDEX = f"{BaseApi.PREFIX}/diagnose"

    @staticmethod
    def get_all(limit: int, offset: int) -> str:
        return f"{DiagnoseApi.INDEX}?limit={limit}&offset={offset}"


user_api = UserApi()
patient_api = PatientApi()
doctor_api = DoctorApi()
diagnose_api = DoctorApi()
