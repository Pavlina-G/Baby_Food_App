import datetime
from http.client import HTTPResponse

from django.shortcuts import render

from baby_food.menu_app.models import MenuWithoutAllergens


def menu_home(request):
    return render(request, 'menus/menu-home.html')


def menu_with_allergens_first(request):

    context = {}


    return render(request, 'menus/menu-with-allergens-first.html', context)


def menu_with_allergens_last(request):
    return render(request, 'menus/menu-with-allergens-last.html')


def menu_no_allergens(request):
    # menus = MenuWithoutAllergens.objects.filter(date__gt=(datetime.date.today() + datetime.timedelta(days=2)))
    menus = MenuWithoutAllergens.objects.all()
    context = {}
    if menus.count() > 5:
        menus_first = menus[:5]
        menus_second = menus[5:10]
        context['menus_first'] = menus_first
        context['menus_second'] = menus_second
    else:
        context['menus_first'] = menus


    return render(request, 'menus/menu-no-allergens.html', context)
