from datetime import date

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDateEdit


class DateInput(QDateEdit):
    def __init__(
        self,
        placeholder: str = "Выберите дату",
        calendar_popup: bool = True,
        display_format: str = "yyyy-MM-dd",
    ):
        super().__init__()

        self.setDisplayFormat(display_format)
        self.setCalendarPopup(calendar_popup)
        self.setDate(QDate.currentDate())

        self.setSpecialValueText(placeholder)

    def value(self) -> date:
        qdate = self.date()

        return date(
            qdate.year(),
            qdate.month(),
            qdate.day(),
        )

    def set_value(self, value: date) -> None:
        self.setDate(QDate(value.year, value.month, value.day))
