from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_order_confirmation(order_id, customer_email, customer_name=None, total_amount=None):
    subject = f"Order Confirmation - #{order_id}"
    greeting = f"Hello {customer_name}," if customer_name else "Hello,"

    message = (
        f"{greeting}\n\n"
        f"Thank you for your order!\n"
        f"Your order ID is {order_id}.\n"
    )

    if total_amount:
        message += f"Total Amount: {total_amount}\n"

    message +=\nWe will notify you once your order is shipped.\n\nBest regards,\nYour Restaurant Team"

    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email],
            fail_silently=False,
        )
        return {"success": True, "message": f"Order confirmation sent to {customer_email}"}

    except BadHeaderError:
        logger.error("Invalid header found when sending order confirmation email.")
        return {"success": False, "message": "Invalid header found."}

    except Exception as e:
        logger.error(f"Error sending email: {e}")
        return {"success": False, "message": f"Error sending email: {str(e)}"}