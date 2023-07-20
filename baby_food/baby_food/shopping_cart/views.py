from django.contrib import messages
from django.shortcuts import render, redirect

from baby_food.accounts.models import Child
from baby_food.menu_app.models import Menu
from baby_food.order.forms import OrderCreateForm
from baby_food.shopping_cart.cart import Cart


def cart_details(request):
    cart = Cart(request)
    return render(request, 'shopping_cart/cart.html')


def add_to_cart(request, pk):
    cart = Cart(request)
    menu = Menu.objects.get(pk=pk)
    cart.add(menu=menu)

    user_pk = request.user
    children = Child.objects.filter(parent_id=user_pk.pk)

    for child in children:
        if child.first_name is None or child.first_name is None:
            messages.info(request, 'Update your profile! Add children data!')
            return redirect(request.META.get('HTTP_REFERER', '/'))

    messages.info(request, 'Menu added to the cart')
    return redirect(request.META.get('HTTP_REFERER', '/'))


def remove_from_cart(request, pk):
    cart = Cart(request)
    menu = Menu.objects.get(pk=pk)
    cart.remove(menu)
    return redirect('cart details')
