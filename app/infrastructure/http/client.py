import httpx
from infrastructure.http.middleware import add_auth_header
from core.app_config import app_config

http = httpx.AsyncClient(
    base_url=app_config.api_url,
    timeout=30.0,
    headers={
        "Content-Type": "application/json",
    },
    event_hooks={"request": [add_auth_header]},
)
