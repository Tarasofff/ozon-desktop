import json
from typing import Optional
from core import app_config
from app.schemas import UserSession
from pydantic import ValidationError

# def save_user(user_data: UserBase) -> None:
#     with open(app_config.user_session_file_path, "w", encoding="utf-8") as f:
#         json.dump(user_data.model_dump(), f, ensure_ascii=False, indent=2)


# def get_user() -> Optional[UserBase]:
#     if not app_config.user_session_file_path.exists():
#         return None
#     with open(app_config.user_session_file_path, "r", encoding="utf-8") as f:
#         return json.load(f)


# def delete_user():
#     if app_config.user_session_file_path.exists():
#         app_config.user_session_file_path.unlink()


def save_user(user_data: UserSession) -> None:
    path = app_config.user_session_file_path
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as f:
        json.dump(
            user_data.model_dump(mode="json"),
            f,
            ensure_ascii=False,
            indent=2,
        )


def get_user() -> Optional[UserSession]:
    path = app_config.user_session_file_path

    if not path.exists():
        return None

    try:
        with path.open("r", encoding="utf-8") as f:
            user_data = json.load(f)

        return UserSession.model_validate(user_data)

    except (json.JSONDecodeError, ValidationError):
        return None


def delete_user() -> None:
    path = app_config.user_session_file_path

    if path.exists():
        path.unlink()
