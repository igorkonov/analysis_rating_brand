from src.models import Product


def test_product_creation():
    """Тест создания продукта."""
    product = Product("iPhone", "apple", 999.0, 4.9)
    assert product.name == "iPhone"
    assert product.brand == "apple"
    assert product.price == 999.0
    assert product.rating == 4.9


def test_product_from_dict():
    """Тест создания продукта из словаря."""
    data = {
        "name": "iPhone",
        "brand": "apple",
        "price": "999",
        "rating": "4.9",
    }
    product = Product.from_dict(data)
    assert product.name == "iPhone"
    assert product.brand == "apple"
    assert product.price == 999.0
    assert product.rating == 4.9


def test_product_from_dict_converts_types():
    """Тест преобразования типов при создании из словаря."""
    data = {
        "name": "iPhone",
        "brand": "apple",
        "price": "999.99",
        "rating": "4.85",
    }
    product = Product.from_dict(data)
    assert isinstance(product.price, float)
    assert isinstance(product.rating, float)
    assert product.price == 999.99
    assert product.rating == 4.85
