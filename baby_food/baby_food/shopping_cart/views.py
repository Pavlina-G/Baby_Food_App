from django.contrib import messages
from django.shortcuts import render, redirect


from baby_food.menu_app.models import Menu
from baby_food.shopping_cart.cart import Cart


def cart_details(request):
    cart = Cart(request)
    return render(request, 'shopping_cart/cart.html')


def add_to_cart(request, pk):
    cart = Cart(request)
    menu = Menu.objects.get(pk=pk)
    cart.add(menu=menu)

    messages.info(request, 'Menu added to the cart')
    return redirect(request.META.get('HTTP_REFERER', '/'))


def remove_from_cart(request, pk):
    cart = Cart(request)
    menu = Menu.objects.get(pk=pk)
    cart.remove(menu)
    return redirect('cart details')
