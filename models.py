from django.db import models
from .utils import calculate_discount

class Order(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,

        STATUS_CHOICES=[
            ("pending", "Pending"),
            ("processing", "Processing"),
            ("completed", "Completed"),
            ("cancelled", "Cancelled"),
        ],
        default="pending"
    )
    
    def __str__(self):
        return f"Order {self.id} - {self.status}"

    def calculate_total(self):
        total = 0
        items = self.items.all()

        for item in items:
            base_cost = item.product.price * item.quantity
            discount_cost = calculate_discount(base_cost, item.product, item.quantity)
            total += discount_cost

        return total

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} - {self.product.name}"