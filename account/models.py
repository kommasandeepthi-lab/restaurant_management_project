from django.db import models
from django.contrib.auth.models import User
from django.db import models
from home.models import MenuItem
from .utils import generate_unique_order_id
from django.utils import timezone
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

class Table(models.Model):
    table_number = models.IntegerField(unique=True, help_text="Unique number assigned to each table.")
    capacity = models.IntegerField(help_text="Maximum number of guests the table can seat.")
    is_available = models.BooleanField(default=True, help_text="Indicate if the table is currently available.")
    loction = models.CharField(max_length=100, help_text="description of where the table is located (e.g., Window Side, Patio".)

    def __str__(self):
        return f"Table {self.table_number} ({'Available' if self.is_available else 'Occupied'})"

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
    name = models.CharField(max_length=100, help_text="Name of the restaurant.")
    description = models.TextField(blank=True, help_text="Optional description of the restaurant.")
    address = models.CharField(blank=True, null=True)

    def get_total_menu_items(self):
        return MenuItem.objects.count()

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

class MenuCategory(models.Model):

        name = models.CharField(max_length=100, unique=True)

        class Meta:
            verbose_name_plural = "Menu Categories"

        def __str__(self):
            return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='items')
    cuisine = models.CharField(max_length=50)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    allergens = models.TextField(blank=True, null=True, help_text="List allergens (e.g. gluten, nuts, dairy)")

    is_daily_special = models.BooleanField(default=Flase)

    def __str__(self):
        base = f"{self.name} - {self.price}"
        if self.allergens:
            return f"{base} (Allergens: {self.allergens})"
        return base

    def __str__(self):
        return self.name

    def get_items_by_cuisine(cls, cuisine_type):
        return cls.objects.filer(cuisine__iexact=cuisine_type)

    @classmethod
    def filter_by_cuisine(cls, cuisine_type):
        return cls.objects.filter(cuisine_type__iexact=cuisine_type)

class OrderStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Menu Item Categories"

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("PROCESSING", "Processing"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    unique_id = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=20. choices=255)
    order_id = models.CharField(max_length=12, unique=True, blank=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, related_name="orders")
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    customer_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_add_now=True)

    status = models.CharField(
        max_length=20
        choices=[("Pending", "Pending"), ("Processing", "Processing"), ("Cancelled", "Cancelled"), ("Completed", "Completed")],
        default="Pending"

        OrderStatus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        related_name="orders"
    )
    created_at = models.DateTimeField(auto_add_now=True)

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = generate_unique_order_id()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Order {self.unique_id} - {self.status}"

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return f"{self.code} ({self.discount_percentage}% off)"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_name} - {self.quantity}"

class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ActiveOrderManager(models.Manager):
    def get_active_orders(self):
        return self.filter(status__in=['pending', 'processing'])

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    customer_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ActiveOrderManager()

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name} ({self.status})"

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)

    operating_days = models.CharField(
        max_length=100,
        help_text="Enter days restaurant is open (e.g. Mon, Tue, Wed, Thu, Fri)"
    )

    def __str__(self):
        return self.name

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


