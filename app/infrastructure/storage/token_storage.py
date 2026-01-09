import keyring
from typing import Optional

APP_NAME = "ozon-desktop"
TOKEN_KEY = "access_token"


def save_token(token: str) -> None:
    keyring.set_password(APP_NAME, TOKEN_KEY, token)


def get_token() -> Optional[str]:
    return keyring.get_password(APP_NAME, TOKEN_KEY)


def delete_token() -> None:
    try:
        keyring.delete_password(APP_NAME, TOKEN_KEY)
    except Exception:
        pass
