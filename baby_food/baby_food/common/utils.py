import datetime

from baby_food.accounts.models import Profile
from baby_food.menus.models import Menu


def is_staff(request):
    return request.user.groups.filter(name='Staff') and not request.user.is_superuser


def get_context_menus(menus):
    context = {}

    if menus.count() > 5:
        menus_first = menus[:5]
        menus_second = menus[5:10]
        context['menus_first'] = menus_first
        context['menus_second'] = menus_second
    else:
        context['menus_first'] = menus

    return context


def get_profile(user_id):
    try:
        profile = Profile.objects.get(user_id=user_id)
    except Profile.DoesNotExist:
        profile = None

    return profile


def get_filtered_menus(age, cat_id):
    menus = Menu.objects.filter(age__exact=age, category_id=cat_id,
                                date__range=(datetime.date.today() + datetime.timedelta(days=1),
                                             datetime.date.today() + datetime.timedelta(days=16)))
    return menus
