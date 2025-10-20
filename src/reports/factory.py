import logging

from .average_rating import AverageRatingReport
from .base import BaseReport

logger = logging.getLogger(__name__)


class ReportFactory:
    """Фабрика для создания экземпляров отчётов по типу."""

    _reports = {
        "average-rating": AverageRatingReport,
    }

    @classmethod
    def create_report(cls, report_type: str) -> BaseReport:
        """Создаёт экземпляр отчёта по типу."""

        logger.debug(f"Создание отчёта типа: {report_type}")
        report_class = cls._reports.get(report_type)

        if report_class is None:
            available = ", ".join(cls._reports.keys())

            logger.error(f"Неизвестный тип отчёта: {report_type}")

            raise ValueError(
                f"Неизвестный тип отчёта: {report_type}.\n"
                f"Доступные отчёты: {available}"
            )
        return report_class()

    @classmethod
    def register_report(cls, report_type: str, report_class: type):
        """Регистрирует новый тип отчёта."""

        logger.info(f"Регистрация нового типа отчёта: {report_type}")

        cls._reports[report_type] = report_class
