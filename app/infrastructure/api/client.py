import httpx
from infrastructure.api.middleware import add_auth_header
from app.core.config.app_config import app_config

http = httpx.AsyncClient(
    base_url=app_config.api_url_v1,
    timeout=30.0,
    headers={
        "Content-Type": "application/json",
    },
    event_hooks={"request": [add_auth_header]},
)
