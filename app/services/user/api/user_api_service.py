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

    async def login_request(self, data):
        pass

    async def registration_request(self, data):
        pass
