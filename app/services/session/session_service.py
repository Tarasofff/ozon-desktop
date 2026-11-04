from schemas.auth import AuthResponse
from schemas.user import UserRead
from infrastructure.storage.token_storage import (
    save_token,
    delete_token,
)
from infrastructure.storage.user_storage import (
    save_user,
    delete_user,
)


class SessionService:

    def save_session(self, data: AuthResponse) -> None:
        try:
            save_token(
                data.token.access_token,
                data.token.token_type,
            )

            user_session = UserRead.model_validate(data.user)
            save_user(user_session)

        except Exception:
            print(f"Ошибка сохранения сессии: {type(e).__name__}: {e}")
            self.clear_session()
            raise

    def clear_session(self) -> None:
        delete_token()
        delete_user()
