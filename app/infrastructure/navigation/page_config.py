from dataclasses import dataclass

from .routes import AppRoutes


@dataclass(frozen=True)
class PageConfig:
    route: AppRoutes
    navigation_title: str
    page_title: str


APP_PAGES = {
    AppRoutes.PATIENTS: PageConfig(
        route=AppRoutes.PATIENTS,
        navigation_title="Пациенты",
        page_title="Список пациентов",
    ),
}
