from django.test import TestCase
from django.contrib.auth.models import User
from home.models import MenuItem
from orders.models import Order, OrderItem
from decimal import Decimal

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="Krishna", password="Radha")
        self.item1 = MenuItem.objects.create(name="Dal", price=Decimal("250.00"))
        self.item2 = MenuItem.objects.create(name="Butter Naan", price=Decimal("50.00"))

        self.order = Order.objects.create(order_id="ORD123", user=self.user)

        OrderItem.objects.create(order=self.order, menu_item=self.item1, quantity=2, price=self.item1.price)
        OrderItem.objects.create(order=self.order, menu_item=self.item2, quantity=3, price=self.item2.price)

    def test_calculate_total(self):
        total = self.order.calculate_total()
        self.assertEqual(total, Decimal("650.00"))