from django.shortcuts import render
from baby_food.common.utils import is_staff, get_context_menus, get_profile, get_filtered_menus


def menu_home(request):
    return render(request, 'menus/menu-home.html')


def menu_with_allergens_first(request):
    user = request.user
    menus = get_filtered_menus('10M-18M', 2)
    profile = get_profile(user.pk)

    context = {'staff_group': is_staff(request)}
    context.update(get_context_menus(menus))
    context['profile'] = profile

    return render(request, 'menus/menu-with-allergens-first.html', context)


def menu_with_allergens_last(request):
    user = request.user
    menus = get_filtered_menus('18M-36M', 2)
    profile = get_profile(user.pk)

    context = {'staff_group': is_staff(request)}
    context.update(get_context_menus(menus))
    context['profile'] = profile

    return render(request, 'menus/menu-with-allergens-last.html', context)


def menu_no_allergens(request):
    user = request.user
    menus = get_filtered_menus('10M-36M', 1)
    profile = get_profile(user.pk)

    context = {'staff_group': is_staff(request)}
    context.update(get_context_menus(menus))
    context['profile'] = profile

    return render(request, 'menus/menu-no-allergens.html', context)
