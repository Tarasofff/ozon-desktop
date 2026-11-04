import httpx
from infrastructure.storage.token_storage import get_token


async def add_auth_header(request: httpx.Request):
    token, type = get_token()
    if token:
        request.headers["Authorization"] = f"{type} {token}"
