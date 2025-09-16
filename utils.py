import string
from orders.models import Coupon

def generate_coupon_code(length: int = 10)

characters = string_uppercase + string.digits

while True:

    code = ''.join(choice(characters) for _ in range(length))

    if not Coupon.objects.filter(code=code).exists():
        return code
