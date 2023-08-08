def is_staff(request):
    return request.user.groups.filter(name='Staff')


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
