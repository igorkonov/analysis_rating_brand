import csv
import logging
from pathlib import Path
from typing import List

from .models import Product

logger = logging.getLogger(__name__)


class CSVFileReader:
    """Класс чтения CSV-файлов, содержащих данные о продукте."""

    def read(self, file_path: str) -> List[Product]:
        """Читает CSV-файл и возвращает список продуктов."""
        logger.debug(f"Чтение файла: {file_path}")
        products = []
        path = Path(file_path)

        with path.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append(Product.from_dict(row))

        logger.debug(f"Прочитано {len(products)} продуктов из {file_path}")
        return products

    def read_multiple(self, file_paths: List[str]) -> List[Product]:
        """
        Читает несколько CSV-файлов и возвращает объединенный список продуктов.
        """
        logger.debug(f"Чтение нескольких файлов: {file_paths}")
        all_products = []
        for file_path in file_paths:
            all_products.extend(self.read(file_path))

        logger.debug(f"Всего прочитано продуктов: {len(all_products)}")
        return all_products
