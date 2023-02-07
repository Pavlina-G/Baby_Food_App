from django import forms
from django.shortcuts import render, redirect

from baby_food.order.forms import OrderCreateForm
from baby_food.order.models import OrderItem
from baby_food.shopping_cart.cart import Cart


def create_order(request):

    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                    address=item['address']
                )
            cart.clear()
        # return redirect('my_orders.html')
        return render(request, 'orders/created_order.html', {'order': order})

    else:
        form = OrderCreateForm()
    return render(request, 'orders/create_order.html', {'form': form})

