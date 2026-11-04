from pathlib import Path
import os


class AppConfig:
    app_name = "Ozon_Desktop"
    api_url_v1 = "http://localhost:8000/v1"

    @property
    def user_session_file_path(self) -> Path:
        app_data_path = Path(os.environ["APPDATA"])
        return app_data_path / self.app_name / "user.json"


app_config = AppConfig()
