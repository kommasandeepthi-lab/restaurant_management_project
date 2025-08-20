from django import template

register = template.Library()

@register.filter
def availability_status(is_available):
    """
    Returns 'Coming Soon' if the item is unavailable,
    otherwise returns an empty string.
    """
    return "" if is_available else "Coming Soon"