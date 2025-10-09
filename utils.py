def calculate_discount(price, discount_percentage):
    try:
        price = float(price)
        discount_percentage = float(discount_percentage)

        if price < 0:
            raise ValueError("Price cannot be negative.")
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        discount_price = price - (price * (discount_percentage / 100))
        return round(discounted_price, 2)

    except (TypeError, ValueError) as e:
        print(f"Error calculating discount: {e}")
        return None