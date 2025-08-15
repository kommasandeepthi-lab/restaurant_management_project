from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    login_form = AuthenticationForm(request, data=request.POST or None)
    return render(request, 'home.html', {'form': login_form})