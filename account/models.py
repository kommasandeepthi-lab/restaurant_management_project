from django.db import models
from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class TodaySpecial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.ImageField(upload_to="menu_images/", blank=True, null=True)


    def __str__(self):
        return self.name

class OpeningHour(models.Model):
    day = models.CharField(max_length=20)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return f"{self.day}: {self.open_time.strtime('%I:%M %p')} - {self.close_time.strftime('%I:%M %p')}"

class Chef(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to="chef_images/", blank=True, null=True)

    def __str__(self):
        return self.name

class RestaurantContact(models.Model)
    address = models.CharField(help_text="Full address of the restaurant")
    phone_number = models.CharField(max_length=15, help_text="Restaurant contact number")
    email = models.EmailField(unique=True, help_text="Official email address")

    class Meta:
        verbose_name = "Restaurant Contact"
        verbose_name_plural = "Restaurant Contacts"

    def __str__(self):
        return f"{self.address} | {self.phone_number} | {self.email}"

class Loction(models.Model)
address = model.CharField(max_length=100)

    def __str__(self):
        return self.address

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total(self):
        return self.product.price * self.quantity

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=0, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}

class OrderStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Menu Categories"

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_add_now=True)

    status = models.ForeignKey(
        OrderStatus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        related_name="orders"
    )

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"