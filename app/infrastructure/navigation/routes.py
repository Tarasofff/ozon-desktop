from enum import StrEnum, auto


class AuthRoutes(StrEnum):
    START = auto()
    LOGIN = auto()
    REGISTRATION = auto()


class AppRoutes(StrEnum):
    PATIENTS = auto()
    DOCTORS = auto()
    NURSES = auto()
    SESSIONS = auto()
