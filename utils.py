def calculate_discount_amount(order_total, discount_percentage):

    try:
        order_total = float(order_total)
        discount_percentage = float(discount_percentage)
    except (TypeError, ValueError):
        raise ValueError("Both order_total and discount_percentage must be numeric values.")

    if order_total < 0:
        raise ValueError("Order total cannot be negative.")
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100.")

    return order_total * (discount_percentage / 100.0)