from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.0
        help_text="Discount percentageto apply to the item price"
    )
    def __str__(self):
        return self.name
    
    def final_price(self) -> float:

        if self.discount_percentage > 0:
            discount_amount = (self.discount_percentage / 100) * float(self.price)
            return round(float(self.price) - discount_amount, 2)
        return float(self.price)