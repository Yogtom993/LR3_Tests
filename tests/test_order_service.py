import pytest
from order_service import OrderService


def test_calculate_item_total_valid_data():
    # Arrange
    service = OrderService()

    # Act
    result = service.calculate_item_total(1000, 2)

    # Assert
    assert result == 2000.0
    # EP: позитивний тест, коректна ціна та кількість


def test_calculate_item_total_negative_price():
    # Arrange
    service = OrderService()

    # Act / Assert
    with pytest.raises(ValueError):
        service.calculate_item_total(-1, 2)
    # BVA: негативний тест, ціна нижче межі 0


def test_calculate_item_total_zero_quantity():
    # Arrange
    service = OrderService()

    # Act / Assert
    with pytest.raises(ValueError):
        service.calculate_item_total(1000, 0)
    # BVA: негативний тест, кількість на межі 0


def test_calculate_item_total_min_quantity():
    # Arrange
    service = OrderService()

    # Act
    result = service.calculate_item_total(1500, 1)

    # Assert
    assert result == 1500.0
    # BVA: позитивний тест, мінімальна допустима кількість


def test_apply_discount_regular_customer():
    # Arrange
    service = OrderService()

    # Act
    result = service.apply_discount(1000, "regular")

    # Assert
    assert result == 1000.0
    # EP: позитивний тест, звичайний покупець без знижки


def test_apply_discount_student_customer():
    # Arrange
    service = OrderService()

    # Act
    result = service.apply_discount(1000, "student")

    # Assert
    assert result == 950.0
    # EP: позитивний тест, студентська знижка 5%


def test_apply_discount_vip_customer():
    # Arrange
    service = OrderService()

    # Act
    result = service.apply_discount(1000, "vip")

    # Assert
    assert result == 900.0
    # EP: позитивний тест, VIP-знижка 10%


def test_apply_discount_unknown_customer_type():
    # Arrange
    service = OrderService()

    # Act / Assert
    with pytest.raises(ValueError):
        service.apply_discount(1000, "unknown")
    # EP: негативний тест, недопустимий тип покупця


def test_delivery_cost_free_delivery_boundary():
    # Arrange
    service = OrderService()

    # Act
    result = service.calculate_delivery_cost(10000, "Київ")

    # Assert
    assert result == 0.0
    # BVA: позитивний тест, межа безкоштовної доставки 10000


def test_delivery_cost_below_free_delivery_boundary():
    # Arrange
    service = OrderService()

    # Act
    result = service.calculate_delivery_cost(9999, "Київ")

    # Assert
    assert result == 150.0
    # BVA: позитивний тест, значення нижче межі безкоштовної доставки


def test_delivery_cost_for_kharkiv():
    # Arrange
    service = OrderService()

    # Act
    result = service.calculate_delivery_cost(5000, "Харків")

    # Assert
    assert result == 80.0
    # EP: позитивний тест, доставка по Харкову


def test_delivery_cost_empty_city():
    # Arrange
    service = OrderService()

    # Act / Assert
    with pytest.raises(ValueError):
        service.calculate_delivery_cost(5000, "")
    # EP: негативний тест, порожнє місто


def test_calculate_order_total_full_order():
    # Arrange
    service = OrderService()

    # Act
    result = service.calculate_order_total(5000, 2, "vip", "Київ")

    # Assert
    assert result == 9150.0
    # EP: позитивний тест, повний розрахунок замовлення