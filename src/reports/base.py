from abc import ABC, abstractmethod
from typing import Any, Dict, List

from ..models import Product


class BaseReport(ABC):
    """Абстрактный базовый класс для отчетов."""

    @abstractmethod
    def generate(self, products: List[Product]) -> Dict[str, Any]:
        """Генерирует отчет и возвращает его в виде словаря."""
        pass
