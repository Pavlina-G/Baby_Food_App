import datetime
from http.client import HTTPResponse

from django.shortcuts import render, redirect

from baby_food.accounts.models import Profile
from baby_food.menu_app.models import Menu


def menu_home(request):
    return render(request, 'menus/menu-home.html')


def menu_with_allergens_first(request):
    user = request.user
    # menus = MenuWithoutAllergens.objects.filter(date__gt=(datetime.date.today() + datetime.timedelta(days=10)))
    menus = Menu.objects.filter(age__exact='10M-18M', category_id=2)
    try:
        profile = Profile.objects.get(user_id=user.id)
    except Profile.DoesNotExist:
        profile = None

    context = {}

    if menus.count() > 5:
        menus_first = menus[:5]
        menus_second = menus[5:10]
        context['menus_first'] = menus_first
        context['menus_second'] = menus_second
    else:
        context['menus_first'] = menus
        context['profile'] = profile

    return render(request, 'menus/menu-with-allergens-first.html', context)


def menu_with_allergens_last(request):
    user = request.user
    # menus = Menu.objects.filter(age__exact='18M-36M', date__gt=(datetime.date.today() + datetime.timedelta(days=10)))
    menus = Menu.objects.filter(age__exact='18M-36M', category_id=2)
    try:
        profile = Profile.objects.get(user_id=user.id)
    except Profile.DoesNotExist:
        profile = None

    context = {}

    if menus.count() > 5:
        menus_first = menus[:5]
        menus_second = menus[5:10]
        context['menus_first'] = menus_first
        context['menus_second'] = menus_second
    else:
        context['menus_first'] = menus
        context['profile'] = profile

    return render(request, 'menus/menu-with-allergens-last.html', context)


def menu_no_allergens(request):
    user = request.user
    # menus = MenuWithoutAllergens.objects.filter(date__gt=(datetime.date.today() + datetime.timedelta(days=10)))
    menus = Menu.objects.filter(age__exact='10M-36M', category_id=1)
    try:
        profile = Profile.objects.get(user_id=user.id)
    except Profile.DoesNotExist:
        profile = None

    context = {}

    if menus.count() > 5:
        menus_first = menus[:5]
        menus_second = menus[5:10]
        context['menus_first'] = menus_first
        context['menus_second'] = menus_second
    else:
        context['menus_first'] = menus
        context['profile'] = profile

    return render(request, 'menus/menu-no-allergens.html', context)
