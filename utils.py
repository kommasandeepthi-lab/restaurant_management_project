import secrets
import string
from .models import Order

def generate_unique_order_id(length=8):
    alphabet = string.ascii_uppercase + string.digits

    while True:
        order_id = ''.join(secrets.cjoice(alphabet) for_in range(length))

        if not Order.objects.filter(order_id=order_id).exists():
            return order_id