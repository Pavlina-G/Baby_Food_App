from http.client import HTTPResponse

from django.shortcuts import render


def menu_home(request):
    return render(request, 'menus/menu-home.html')


def menu_with_allergens_first(request):
    context = {}


    return render(request, 'menus/menu-with-allergens-first.html', context)


def menu_with_allergens_last(request):
    return render(request, 'menus/menu-with-allergens-last.html')


def menu_no_allergens(request):
    context = {}
    context['list_numbers'] = [1, 2, 3, 4, 5]
    return render(request, 'menus/menu-no-allergens.html', context)
