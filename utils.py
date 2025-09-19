from django.core.mail import send_mail, BadHeaderError
from django.core.exceptions import ValidationError
from django.core validators import validate_email
from django.conf import settings

def send_app_email(recipient_email: str, subject: str, message: str) -> bool:
    try:
        validate_email(recipient_email)

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient_email],
            fail_silently=False,
        )
        return True

    except ValidationError:
        print(f"Invalid email: {recipient_email}")
        return False

    except BadHeaderError:
        print("Invalid header found.")
        return False

    except Exception as e:
        print(f"Error sending email: {e}")
        return False