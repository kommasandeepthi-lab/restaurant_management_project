from django.shortcuts import render
from .dorms import ConatactForm

def contact_view(request):
    if request.method == "POST:
        form = ConatactForm(request.POST)
        if form.is_valid()

           return render(request, 'contact_success.html')
    else:
        form = ConatactForm()

    return render(request, 'contact.html', {'form': form})