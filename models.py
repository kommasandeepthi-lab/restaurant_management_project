from django.db import models
from django.contrib.auth.models import User
from homr.models import MenuItem

class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    comment = models.TextField(blank=True, nul=True)
    review_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'menu_item')
        ordering = ['-review_date']

    def __str__(self):
        return f"Review by {self.user.username} on {self.menu_item.name}"