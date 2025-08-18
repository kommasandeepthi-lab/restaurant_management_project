from django.db import models

class RestaurantInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='restaurant/', blank=True, null=True)

    def __str__(self):
        return self.name