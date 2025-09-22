from django.db import models

class OrderManager(models.Manager):
    def with_status(self, status):
        return self.filter(status=status)

    def pending(self):
        return self.filter(status="pending")

    def processing(self):
        return self.filter(status="processing")

    def completed(self):
        return self.filter(status="completed")

class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    customer = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    objects = OrderManager()

    def __str__(self):
        return f"Order {self.id} - {self.status}"