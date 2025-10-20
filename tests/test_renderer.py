import sys
from io import StringIO
from unittest.mock import patch

from src.reports.renderer import ConsoleRenderer


def test_tabulate_import_error():
    """Тест случая, когда библиотека tabulate не может быть импортирована."""
    # Сохраняем оригинальный модуль
    import src.reports.renderer

    original_tabulate = getattr(src.reports.renderer, "tabulate", None)

    try:
        # Симулируем ошибку импорта
        with patch.dict("sys.modules", {"tabulate": None}):
            # Перезагружаем модуль для срабатывания ImportError
            import importlib

            importlib.reload(src.reports.renderer)

            assert not src.reports.renderer.TABULATE_AVAILABLE
    finally:
        # Восстанавливаем оригинальное состояние
        if original_tabulate:
            src.reports.renderer.tabulate = original_tabulate
            src.reports.renderer.TABULATE_AVAILABLE = True


def test_renderer_with_data():
    """Тест рендеринга отчёта с данными."""
    renderer = ConsoleRenderer()
    report_data = {
        "headers": ["brand", "rating"],
        "rows": [("apple", 4.85), ("samsung", 4.7)],
    }

    # Перехватываем вывод
    captured_output = StringIO()
    sys.stdout = captured_output

    renderer.render(report_data)

    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

    # Проверяем, что в выводе есть данные
    assert "apple" in output
    assert "samsung" in output
    assert "4.85" in output
    assert "4.7" in output


def test_renderer_empty_data():
    """Тест рендеринга пустого отчёта."""
    renderer = ConsoleRenderer()
    report_data = {"headers": ["brand", "rating"], "rows": []}

    # Перехватываем вывод
    captured_output = StringIO()
    sys.stdout = captured_output

    renderer.render(report_data)

    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

    # Проверяем, что есть заголовки
    assert "brand" in output
    assert "rating" in output


def test_renderer_without_tabulate():
    """Тест рендеринга при отсутствии библиотеки tabulate."""
    with patch("src.reports.renderer.TABULATE_AVAILABLE", False):
        renderer = ConsoleRenderer()
        report_data = {
            "headers": ["brand", "rating"],
            "rows": [("apple", 4.85), ("samsung", 4.7)],
        }

        captured_output = StringIO()
        sys.stdout = captured_output

        renderer.render(report_data)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Проверяем формат простого вывода
        assert "1 | apple | 4.85" in output
        assert "2 | samsung | 4.7" in output
        assert "-" * 10 in output  # Проверяем наличие разделительной линии


def test_renderer_without_headers():
    """Тест рендеринга данных без заголовков."""
    with patch("src.reports.renderer.TABULATE_AVAILABLE", False):
        renderer = ConsoleRenderer()
        report_data = {
            "headers": [],
            "rows": [("apple", 4.85), ("samsung", 4.7)],
        }

        captured_output = StringIO()
        sys.stdout = captured_output

        renderer.render(report_data)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Проверяем формат вывода без заголовков
        assert "1 | apple | 4.85" in output
        assert "2 | samsung | 4.7" in output
