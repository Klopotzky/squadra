from django.shortcuts import render, redirect

# from django.contrib.auth.forms import UserCreationForm
# UserCreationForm Importowane w .forms
from django.contrib import messages
from .forms import UserRegister
from django.contrib.auth.models import User, auth


# Create your views here.

def create_user(reqest):
    if reqest.method == 'POST':    
        form = UserRegister(reqest.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(reqest, f'Konto dla {username}!')
            return redirect('login')
            print('saved')
    else:
        form = UserRegister()

    return render(reqest, 'user/register.html', {'form': form})


def logout(reqest):
    auth.logout(reqest)
    return redirect('login')


def home(request, *args, **kwargs):
    if request.user.is_authenticated:
        return render(request, 'user/home.html')
    else:
        return redirect('login')
    
