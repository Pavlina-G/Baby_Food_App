from http.client import HTTPResponse

from django.shortcuts import render

def menus_home(request):
    return render(request, 'menus/../../templates/nicepage/menus.html')

def menus_with_allergens(request):
    return render(request, 'menus/../../templates/nicepage/menus-with-allergens-details.html')

def menus_no_allergens(request):
    return render(request, 'menus/../../templates/nicepage/menus-no-allergens-details.html')
