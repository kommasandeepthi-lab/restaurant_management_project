from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db import DatabaseError

# Create your views here.
def signup_view(request):
    try:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully. Please log in.')
                return redirect('login')
        else:
            form = UserCreationForm()

        return render(request, 'signup.html', {'form': form})

    except DatabaseError as e:

        messages.error(request, 'A database error occurred. Please try again later.')
        return render(request, 'signup.html', {'form': UserCreationForm()})

    except Exception as e:

        messages.error(request, 'An unexpected error occurred. Please try again.')
        return render(request, 'signup.html', {'form': UserCreationForm()})