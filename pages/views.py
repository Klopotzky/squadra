from django.http import HttpResponse
from django.shortcuts import render
from .models import Pages

# Create your views here.


def home(request, *args, **kwargs):
    info = Pages.objects.all().order_by('autor')
    return render(request, 'pages/home.html', {'info': info})


def home2(request, *args, **kwargs):
    return render(request, 'pages/base2.html', {})
