import argparse
import logging
import sys
from pathlib import Path

from src.config_logging import setup_logging
from src.file_reader import CSVFileReader
from src.reports.factory import ReportFactory
from src.reports.renderer import ConsoleRenderer

logger = logging.getLogger(__name__)


def parse_arguments():
    """Парсит аргументы командной строки."""
    parser = argparse.ArgumentParser(
        description="Analyze product ratings and generate reports"
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to CSV files with product data",
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Report type to generate (e.g., average-rating)",
    )

    return parser.parse_args()


def validate_files(file_paths):
    """Проверяет существование и доступность файлов."""
    errors = []
    for file_path in file_paths:
        path = Path(file_path)
        if not path.exists():
            errors.append(f"File not found: {file_path}")
            logger.error(f"Файл не найден: {file_path}")
        elif not path.is_file():
            errors.append(f"Not a file: {file_path}")
            logger.error(f"Не является файлом: {file_path}")
    return errors


def main():
    """Основная функция выполнения."""
    setup_logging()

    args = parse_arguments()

    logger.info("Запуск анализа рейтинга брендов")

    # Валидация файлов
    file_errors = validate_files(args.files)
    if file_errors:
        logger.error("Предоставлены некорректные файлы")
        sys.exit(1)

    # Чтение данных из всех файлов
    reader = CSVFileReader()
    try:
        logger.info(f"Чтение {len(args.files)} файл(ов)")
        data = reader.read_multiple(args.files)
        logger.info(f"Успешно прочитано {len(data)} продуктов")
    except Exception as e:
        logger.exception(f"Ошибка при чтении файлов: {e}")
        sys.exit(1)

    # Генерация отчёта
    try:
        logger.info(f"Создание отчёта типа: {args.report}")
        report = ReportFactory.create_report(args.report)
        result = report.generate(data)
        logger.info("Отчёт успешно сгенерирован")
    except ValueError as e:
        logger.error(str(e))
        sys.exit(1)
    except Exception as e:
        logger.exception(f"Ошибка при генерации отчёта: {e}")
        sys.exit(1)

    # Вывод отчёта
    try:
        logger.info("Вывод отчёта")
        renderer = ConsoleRenderer()
        renderer.render(result)
    except Exception as e:
        logger.exception(f"Ошибка при выводе отчёта: {e}")
        sys.exit(1)

    logger.info("Анализ завершён успешно")


if __name__ == "__main__":
    main()
