from http.client import HTTPResponse

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def menus(request):
    return render(request, 'menus/Menus.html')
