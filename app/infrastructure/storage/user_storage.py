import json
from typing import Optional
from models.user_model import UserModel
from core import app_config


def save_user(user_data: UserModel):
    with open(app_config.user_session_file_path, "w", encoding="utf-8") as f:
        json.dump(user_data.model_dump(), f, ensure_ascii=False, indent=2)


def get_user() -> Optional[UserModel]:
    if not app_config.user_session_file_path.exists():
        return None
    with open(app_config.user_session_file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def delete_user():
    if app_config.user_session_file_path.exists():
        app_config.user_session_file_path.unlink()
