from dataclasses import dataclass


@dataclass
class Product:
    """
    Класс, представляющий продукт с его атрибутами.
    """
    name: str
    brand: str
    price: float
    rating: float

    @classmethod
    def from_dict(cls, data: dict):
        """Создает экземпляр Product из словаря."""
        return cls(
            name=data["name"],
            brand=data["brand"],
            price=float(data["price"]),
            rating=float(data["rating"]),
        )
