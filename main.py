import argparse
import logging
import sys
from pathlib import Path

from src.config_logging import setup_logging
from src.file_reader import CSVFileReader

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
    setup_logging()

    args = parse_arguments()

    logger.info("Запуск анализа рейтинга брендов")

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

        logger.info(f"Запрошен тип отчёта: {args.report}")
        logger.info("Примеры прочитанных продуктов:")
        for product in data[:3]:
            logger.info(
                f"  {product.name} ({product.brand}): "
                f"${product.price}, рейтинг: {product.rating}"
            )

    except Exception as e:
        logger.exception(f"Ошибка при чтении файлов: {e}")
        sys.exit(1)

    logger.warning("Генерация отчётов пока не реализована")


if __name__ == "__main__":
    main()
