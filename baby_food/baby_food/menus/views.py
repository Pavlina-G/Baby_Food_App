import datetime

from django.shortcuts import render

from baby_food.accounts.models import Profile
from baby_food.common.utils import is_staff, get_context_menus
from baby_food.menus.models import Menu


def menu_home(request):
    return render(request, 'menus/menu-home.html')


def menu_with_allergens_first(request):
    user = request.user
    menus = Menu.objects.filter(age__exact='10M-18M', category_id=2,
                                date__range=(datetime.date.today() + datetime.timedelta(days=1),
                                             datetime.date.today() + datetime.timedelta(days=12)))

    try:
        profile = Profile.objects.get(user_id=user.id)
    except Profile.DoesNotExist:
        profile = None

    context = {'staff_group': is_staff(request)}
    context.update(get_context_menus(menus))
    context['profile'] = profile

    return render(request, 'menus/menu-with-allergens-first.html', context)


def menu_with_allergens_last(request):
    user = request.user
    menus = Menu.objects.filter(age__exact='18M-36M', category_id=2,
                                date__range=(datetime.date.today() + datetime.timedelta(days=1),
                                             datetime.date.today() + datetime.timedelta(days=12)))

    try:
        profile = Profile.objects.get(user_id=user.id)
    except Profile.DoesNotExist:
        profile = None

    context = {'staff_group': is_staff(request)}
    context.update(get_context_menus(menus))
    context['profile'] = profile

    return render(request, 'menus/menu-with-allergens-last.html', context)


def menu_no_allergens(request):
    user = request.user
    menus = Menu.objects.filter(age__exact='10M-36M', category_id=1,
                                date__range=(datetime.date.today() + datetime.timedelta(days=1),
                                             datetime.date.today() + datetime.timedelta(days=12)))

    try:
        profile = Profile.objects.get(user_id=user.id)
    except Profile.DoesNotExist:
        profile = None

    context = {'staff_group': is_staff(request)}
    context.update(get_context_menus(menus))
    context['profile'] = profile

    return render(request, 'menus/menu-no-allergens.html', context)
