from django.db import models

class Restaurant(models.Model)
    name = models.CharField(max_length=100)
    history = models.TextField()
    mission = models.TextField()
    logo = models.ImageField(upload_to='restaurant_logos/')

    def __str__(self):
        return self.name