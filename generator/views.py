from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    password = ""

    length = int(request.GET.get('length', 12))
    chars = list("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get('uppercase') == "on":
        chars.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get('numbers') == "on":
        chars.extend(list("0123456789"))
    if request.GET.get('special') == "on":
        chars.extend(list("~!@#$%^&*()_+`"))

    for num in range(length):
        password += random.choice(chars)

    return render(request, 'generator/password.html',
         {'password': password})


def about(request):
    return render(request, 'generator/about.html')
