from pathlib import Path
from PySide6.QtCore import QStandardPaths


class AppConfig:
    app_name = "Ozon_Desktop"
    api_url_v1 = "http://localhost:8000/v1"

    @property
    def user_session_file_path(self) -> Path:
        app_data_path = QStandardPaths.writableLocation(
            QStandardPaths.StandardLocation.AppDataLocation
        )
        return Path(app_data_path) / "user.json"


app_config = AppConfig()
