from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import RestaurantAddress

def contact_view(request):
    address = RestaurantAddress.objects.first()

    if request.method == "POST";
       form = ContactForm(request.POST)
       if form.is_valid():
        return redirect("thank_you")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form, "address": address})