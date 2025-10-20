import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

try:
    from tabulate import tabulate

    TABULATE_AVAILABLE = True
except ImportError:
    TABULATE_AVAILABLE = False
    logger.warning(
        "Библиотека tabulate не установлена, будет упрощённый вывод"
    )


class ConsoleRenderer:
    """Рендерит отчёты в консоль."""

    def render(self, report_data: Dict[str, Any]) -> None:
        """Выводит данные отчёта в консоль в виде таблицы."""
        headers = report_data.get("headers", [])
        rows = report_data.get("rows", [])

        logger.debug(f"Рендеринг отчёта: {len(rows)} строк")

        if TABULATE_AVAILABLE:

            print(
                tabulate(
                    rows,
                    headers=headers,
                    tablefmt="grid",
                    showindex=range(1, len(rows) + 1),
                )
            )
        else:
            self._render_simple(headers, rows)

    def _render_simple(self, headers: list, rows: list) -> None:
        """Простой запасной рендеринг без tabulate."""
        if headers:
            print("   | " + " | ".join(str(h) for h in headers))
            print("-" * 50)
        for idx, row in enumerate(rows, start=1):
            print(f" {idx} | " + " | ".join(str(cell) for cell in row))
