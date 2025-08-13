from django import template

register = template.Library()

@register.filter
def friendly_datetime(value):
    """
    Custom filter to diaplay datetime in a friendly format.
    Example: 'Tuesday, 13 August 2025 at 2:35 PM'
    """
    if value is None:
        return ""
    return value.strftime(%A, %d %B %Y at %I:%M %p)