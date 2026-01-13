import keyring
from typing import Optional
from core import app_config

_APP_NAME = app_config.app_name
_TOKEN_KEY = "access_token"
_TOKEN_TYPE_KEY = "token_type"


def save_token(token: str, token_type: str) -> None:
    for key, value in ((_TOKEN_KEY, token), (_TOKEN_TYPE_KEY, token_type)):
        keyring.set_password(_APP_NAME, key, value)


def get_token() -> tuple[Optional[str], Optional[str]]:
    token = keyring.get_password(_APP_NAME, _TOKEN_KEY)
    token_type = keyring.get_password(_APP_NAME, _TOKEN_TYPE_KEY)
    return token, token_type


def delete_token() -> None:
    try:
        for key in (_TOKEN_KEY, _TOKEN_TYPE_KEY):
            keyring.delete_password(_APP_NAME, key)
    except Exception:
        pass
