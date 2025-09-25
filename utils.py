from typing List, Dict, Union

def calculate_order_total(order_items: List[Dict[str, Union[int, float]]]) -> float:

    if not order_items:
        return 0.0

    total_cost = 0.0

    for item in order_items:

        quantity = int(item.get("quantity", 0))
        price = float(item.get("price", 0.0))

        if quantity < 0 or price < 0:
            continue

        total_cost += quantity * price

    return round(total_cost, 2)