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

class RestaurantInfo(models.Model)
address = models.CharField(max_length=255)

    def __str__(self):
        return self.address

class Loction(models.Model)
address = model.CharField(max_length=100)

    def __str__(self):
        return self.address