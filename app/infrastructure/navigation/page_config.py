from dataclasses import dataclass

from .routes import AppRoutes


@dataclass(frozen=True)
class PageConfig:
    route: AppRoutes
    navigation_title: str
    page_title: str


APP_PAGES = {
    AppRoutes.SESSIONS: PageConfig(
        route=AppRoutes.SESSIONS,
        navigation_title="Сессии",
        page_title="Список сессий",
    ),
    AppRoutes.PATIENTS: PageConfig(
        route=AppRoutes.PATIENTS,
        navigation_title="Пациенты",
        page_title="Список пациентов",
    ),
    AppRoutes.DOCTORS: PageConfig(
        route=AppRoutes.DOCTORS,
        navigation_title="Врачи",
        page_title="Список врачей",
    ),
    AppRoutes.NURSES: PageConfig(
        route=AppRoutes.NURSES,
        navigation_title="Медсестры",
        page_title="Список медсестёр",
    ),
}
