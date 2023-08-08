from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from baby_food.accounts.models import Child, Profile
from baby_food.menu_app.models import Menu

from baby_food.shopping_cart.cart import Cart


def cart_details(request):
    cart = Cart(request)
    return render(request, 'shopping_cart/cart.html')


@login_required
def add_to_cart(request, pk):
    cart = Cart(request)
    menu = Menu.objects.get(pk=pk)

    staff_group = request.user.groups.filter(name='Staff')
    if staff_group:
        messages.info(request, 'You are not allowed to buy menus.')
        return redirect(request.META.get('HTTP_REFERER', '/'))

    user = request.user
    children = Child.objects.filter(parent_id=user.pk)
    location = Profile.objects.get(user_id=user.pk).location

    if location is None:
        messages.info(request, 'Please update your profile. Add address.')
        return redirect(request.META.get('HTTP_REFERER', '/'))

    for child in children:
        if child.first_name is None or child.last_name is None:
            messages.info(request, 'Please update your profile. Add children data.')
            return redirect(request.META.get('HTTP_REFERER', '/'))

    cart.add(menu=menu)

    messages.info(request, 'Menu added to the cart')
    return redirect(request.META.get('HTTP_REFERER', '/'))


def remove_from_cart(request, pk):
    cart = Cart(request)
    menu = Menu.objects.get(pk=pk)
    cart.remove(menu)
    return redirect('cart details')
