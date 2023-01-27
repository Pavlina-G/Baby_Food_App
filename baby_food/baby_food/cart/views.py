from django.shortcuts import render

# from baby_food.cart.cart import Cart


def cart_details(request):
    return render(request, 'cart/cart.html')


# def add_to_cart(request, menu_id):
#     cart = Cart(request)
#     cart.add(menu_id)
#
#     return render(request, 'cart/menu-cart.html')
#
#
# def cart(request):
#     return render(request, 'cart/cart.html')
#
#
# def checkout(request):
#     return render(request, 'cart/checkout.html')
