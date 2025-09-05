from .models import SiteInfo

def restaurant_address(request):
    try:
        address = SiteInfo.objects.first().address
    except AttributeError:
        address = "Address not set"
    return {"restaurant_address": address}