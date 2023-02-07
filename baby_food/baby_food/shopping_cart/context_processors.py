from baby_food.shopping_cart.cart import Cart


def cart(request):
    return {'cart': Cart(request)}