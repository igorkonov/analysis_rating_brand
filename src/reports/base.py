from abc import ABC, abstractmethod
from typing import List, Dict, Any

from ..models import Product


class BaseReport(ABC):
    """Абстрактный базовый класс для отчетов."""

    @abstractmethod
    def generate(self, products: List[Product]) -> Dict[str, Any]:
        """Генерирует отчет и возвращает его в виде словаря."""
        pass
