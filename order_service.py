class OrderService:
    """
    Сервіс для розрахунку вартості замовлення в інтернет-магазині техніки.
    Містить логіку розрахунку товарів, знижок та доставки.
    """

    DISCOUNT_RATES = {
        "regular": 0.00,
        "student": 0.05,
        "vip": 0.10
    }

    def calculate_item_total(self, price: float, quantity: int) -> float:
        """
        Обчислює загальну вартість одного товару за ціною та кількістю.
        """
        if price < 0:
            raise ValueError("Ціна товару не може бути від'ємною")

        if quantity <= 0:
            raise ValueError("Кількість товару має бути більшою за 0")

        total = price * quantity
        return round(total, 2)

    def apply_discount(self, amount: float, customer_type: str) -> float:
        """
        Застосовує знижку залежно від типу покупця.
        """
        if amount < 0:
            raise ValueError("Сума замовлення не може бути від'ємною")

        if customer_type not in self.DISCOUNT_RATES:
            raise ValueError("Невідомий тип покупця")

        discount = self.DISCOUNT_RATES[customer_type]
        final_amount = amount - (amount * discount)

        return round(final_amount, 2)

    def calculate_delivery_cost(self, amount: float, city: str) -> float:
        """
        Обчислює вартість доставки.
        Якщо сума замовлення від 10000 грн — доставка безкоштовна.
        Для Харкова доставка дешевша, для інших міст дорожча.
        """
        if amount < 0:
            raise ValueError("Сума замовлення не може бути від'ємною")

        if not city or not city.strip():
            raise ValueError("Місто доставки не може бути порожнім")

        if amount >= 10000:
            return 0.0

        normalized_city = city.strip().lower()

        if normalized_city == "харків":
            return 80.0

        return 150.0

    def calculate_order_total(self, price: float, quantity: int, customer_type: str, city: str) -> float:
        """
        Обчислює фінальну суму замовлення з урахуванням кількості,
        знижки та доставки.
        """
        item_total = self.calculate_item_total(price, quantity)
        discounted_total = self.apply_discount(item_total, customer_type)
        delivery = self.calculate_delivery_cost(discounted_total, city)

        return round(discounted_total + delivery, 2)