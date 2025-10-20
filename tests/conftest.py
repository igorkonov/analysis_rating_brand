import csv
import tempfile
from pathlib import Path

import pytest

from src.models import Product


@pytest.fixture
def sample_products():
    """Тестовые данные продуктов."""
    return [
        Product("iPhone 15", "apple", 999.0, 4.9),
        Product("iPhone 14", "apple", 799.0, 4.8),
        Product("Galaxy S23", "samsung", 899.0, 4.7),
        Product("Redmi Note 12", "xiaomi", 199.0, 4.6),
    ]


@pytest.fixture
def temp_csv_file():
    """Создаёт временный CSV файл с тестовыми данными."""
    with tempfile.NamedTemporaryFile(
        mode="w", delete=False, suffix=".csv", newline="", encoding="utf-8"
    ) as f:
        writer = csv.writer(f)
        writer.writerow(["name", "brand", "price", "rating"])
        writer.writerow(["iPhone 15", "apple", "999", "4.9"])
        writer.writerow(["Galaxy S23", "samsung", "899", "4.7"])
        temp_path = f.name

    yield temp_path

    Path(temp_path).unlink(missing_ok=True)


@pytest.fixture
def temp_csv_files():
    """Создаёт несколько временных CSV файлов."""
    files = []

    # Файл 1
    with tempfile.NamedTemporaryFile(
        mode="w", delete=False, suffix=".csv", newline="", encoding="utf-8"
    ) as f:
        writer = csv.writer(f)
        writer.writerow(["name", "brand", "price", "rating"])
        writer.writerow(["iPhone 15", "apple", "999", "4.9"])
        writer.writerow(["iPhone 14", "apple", "799", "4.8"])
        files.append(f.name)

    # Файл 2
    with tempfile.NamedTemporaryFile(
        mode="w", delete=False, suffix=".csv", newline="", encoding="utf-8"
    ) as f:
        writer = csv.writer(f)
        writer.writerow(["name", "brand", "price", "rating"])
        writer.writerow(["Galaxy S23", "samsung", "899", "4.7"])
        writer.writerow(["Redmi Note 12", "xiaomi", "199", "4.6"])
        files.append(f.name)

    yield files

    for file_path in files:
        Path(file_path).unlink(missing_ok=True)
