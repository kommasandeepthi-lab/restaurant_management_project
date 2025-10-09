from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Order

@receiver(post_save, sender=Order)
def send_status_update_email(sender, instance, created, **kwargs):
    if created:
        return 

    try:
        previous_order = Order.objects.get(pk=instance.pk)
    except Order.DoesNotExist:
        return
    
    if previous_order.status != instance.status:
        subject = f"Order #{instance.id} Status Updated"
        message = (
            f"Hello Admin, \n\n"
            f"The status of Order #{instance.id} has been updated.\n"
            f"Previous Status: {previous_order.status}\n"
            f"New Status: {instance.status}\n\n"
            f"Please log in to the admin dashboard for details.\n\n"
            f"Best Regards, \n"
            f"Your Restaurant System"
        )