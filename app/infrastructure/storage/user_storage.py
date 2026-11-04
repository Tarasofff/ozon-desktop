import json
from typing import Optional
from core import app_config
from app.schemas import UserRead
from pydantic import ValidationError


def save_user(user_data: UserRead) -> None:
    path = app_config.user_session_file_path
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as f:
        json.dump(
            user_data.model_dump(mode="json"),
            f,
            ensure_ascii=False,
            indent=2,
        )


def get_user() -> Optional[UserRead]:
    path = app_config.user_session_file_path

    if not path.exists():
        return None

    try:
        with path.open("r", encoding="utf-8") as f:
            user_data = json.load(f)

        return UserRead.model_validate(user_data)

    except (json.JSONDecodeError, ValidationError):
        return None


def delete_user() -> None:
    path = app_config.user_session_file_path

    if path.exists():
        path.unlink()
