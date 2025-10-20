import pytest

from src.reports.average_rating import AverageRatingReport
from src.reports.base import BaseReport
from src.reports.factory import ReportFactory


def test_create_average_rating_report():
    """Тест создания отчёта average-rating."""
    report = ReportFactory.create_report("average-rating")
    assert isinstance(report, AverageRatingReport)
    assert isinstance(report, BaseReport)


def test_create_unknown_report():
    """Тест создания несуществующего отчёта."""
    with pytest.raises(ValueError) as exc_info:
        ReportFactory.create_report("unknown-report")

    assert "Неизвестный тип отчёта" in str(exc_info.value)
    assert "unknown-report" in str(exc_info.value)
    assert "average-rating" in str(exc_info.value)


def test_register_new_report():
    """Тест регистрации нового типа отчёта."""

    class CustomReport(BaseReport):
        def generate(self, products):
            return {"headers": [], "rows": []}

    ReportFactory.register_report("custom", CustomReport)
    report = ReportFactory.create_report("custom")
    assert isinstance(report, CustomReport)
