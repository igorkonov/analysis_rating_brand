from src.reports.average_rating import AverageRatingReport


def test_average_rating_report(sample_products):
    """Тест генерации отчёта по среднему рейтингу."""
    report = AverageRatingReport()
    result = report.generate(sample_products)

    assert "headers" in result
    assert "rows" in result
    assert result["headers"] == ["brand", "rating"]
    assert len(result["rows"]) == 3

    # Проверяем сортировку по убыванию рейтинга
    ratings = [row[1] for row in result["rows"]]
    assert ratings == sorted(ratings, reverse=True)

    # Проверяем средний рейтинг Apple: (4.9 + 4.8) / 2 = 4.85
    apple_row = [row for row in result["rows"] if row[0] == "apple"][0]
    assert apple_row[1] == 4.85


def test_average_rating_empty_data():
    """Тест генерации отчёта с пустыми данными."""
    report = AverageRatingReport()
    result = report.generate([])

    assert result["headers"] == ["brand", "rating"]
    assert result["rows"] == []


def test_average_rating_single_brand(sample_products):
    """Тест генерации отчёта для одного бренда."""
    report = AverageRatingReport()
    single_brand = [p for p in sample_products if p.brand == "samsung"]
    result = report.generate(single_brand)

    assert len(result["rows"]) == 1
    assert result["rows"][0][0] == "samsung"
    assert result["rows"][0][1] == 4.7


def test_average_rating_rounding(sample_products):
    """Тест округления среднего рейтинга."""
    report = AverageRatingReport()
    result = report.generate(sample_products)

    # Проверяем, что все рейтинги округлены до 2 знаков
    for row in result["rows"]:
        rating = row[1]
        assert isinstance(rating, float)
        # Проверяем, что не более 2 знаков после запятой
        assert len(str(rating).split(".")[-1]) <= 2 or rating == int(rating)
