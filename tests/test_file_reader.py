import pytest
from src.file_reader import CSVFileReader
from src.models import Product


def test_read_single_file(temp_csv_file):
    """Тест чтения одного CSV файла."""
    reader = CSVFileReader()
    products = reader.read(temp_csv_file)

    assert len(products) == 2
    assert isinstance(products[0], Product)
    assert products[0].name == "iPhone 15"
    assert products[0].brand == "apple"
    assert products[0].price == 999.0
    assert products[0].rating == 4.9


def test_read_multiple_files(temp_csv_files):
    """Тест чтения нескольких CSV файлов."""
    reader = CSVFileReader()
    products = reader.read_multiple(temp_csv_files)

    assert len(products) == 4
    brands = {p.brand for p in products}
    assert brands == {"apple", "samsung", "xiaomi"}


def test_read_nonexistent_file():
    """Тест чтения несуществующего файла."""
    reader = CSVFileReader()
    with pytest.raises(FileNotFoundError):
        reader.read("nonexistent.csv")


def test_read_empty_list():
    """Тест чтения пустого списка файлов."""
    reader = CSVFileReader()
    products = reader.read_multiple([])
    assert products == []
