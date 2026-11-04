from pathlib import Path


class AppConfig:
    app_name = "Ozon_Desktop"
    api_url_v1 = "http://localhost:8000/v1"
    user_session_file_path = Path.home() / f".{app_name}_user.json"


app_config = AppConfig()
