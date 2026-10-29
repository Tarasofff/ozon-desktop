from core.constants import user_api
from infrastructure.http.client import http

# class UserApiService:

#     async def login_request(
#         self, data: UserLoginModel
#     ) -> tuple[bool, UserAuthResponseModel]:
#         response = await http.post(
#             user_api.LOGIN,
#             json=data.model_dump(),
#         )

#         return response.status_code == 200, response.json()

#     async def registration_request(
#         self, data: UserRegistrationModel
#     ) -> tuple[bool, UserAuthResponseModel]:
#         response = await http.post(
#             user_api.REGISTRATION,
#             json=data.model_dump(),
#         )

#         return response.status_code == 201, response.json()


class UserApiService:

    async def login_request(self, data: UserLoginModel):
        pass

    async def registration_request(self, data: UserRegistrationModel):
        pass
