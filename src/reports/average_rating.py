import logging
from collections import defaultdict
from typing import List, Dict, Any

from .base import BaseReport
from ..models import Product


logger = logging.getLogger(__name__)


class AverageRatingReport(BaseReport):
    """Отчет по среднему рейтингу продуктов по брендам."""

    def generate(self, products: List[Product]) -> Dict[str, Any]:
        """Генерирует отчет со средним рейтингом по брендам."""

        if not products:
            logger.warning("Список продуктов пуст")
            return {"headers": ["brand", "rating"], "rows": []}

        brand_ratings = defaultdict(list)
        for product in products:
            brand_ratings[product.brand].append(product.rating)

        brand_averages = []
        for brand, ratings in brand_ratings.items():
            avg_rating = sum(ratings) / len(ratings)
            brand_averages.append((brand, round(avg_rating, 2)))

        brand_averages.sort(key=lambda x: x[1], reverse=True)

        logger.debug(f"Сгенерирован отчёт для {len(brand_averages)} брендов")

        return {
            "headers": ["brand", "rating"],
            "rows": brand_averages,
        }
