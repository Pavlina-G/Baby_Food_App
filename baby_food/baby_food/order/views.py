from django import forms

from django.shortcuts import render, redirect

from baby_food.accounts.models import Profile
from baby_food.common.models import Location
from baby_food.order.forms import OrderCreateForm
from baby_food.order.models import OrderItem, Order
from baby_food.shopping_cart.cart import Cart


def create_order(request):
    cart = Cart(request)
    user_pk = request.user.pk
    order_customer = Profile.objects.get(user_id=user_pk)
    customer_address = Location.objects.get(pk=order_customer.location_id)

    if request.method == 'POST':
        # form = OrderCreateForm(request.POST, initial={'customer': order_customer, 'address': customer_address})
        form = OrderCreateForm(request.POST, initial={'customer': order_customer, 'address': customer_address})
        if form.is_valid():
            order = form.save(commit=False)
            order.customer=order_customer
            order.address = customer_address
            order.save()
    # order.customer = Profile.objects.get(user_id=user_pk)
    # order.address = Profile.objects.get(user_id=user_pk).location
    # form.save()
    # order.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['menu'],
                    price=item['price'],
                    quantity=item['quantity'],
                    address=item['location']
                )
            cart.clear()
    # return redirect('my_orders.html')
        return redirect('created order')


# return render(request, 'orders/created_order.html', {'order': order})

    else:
        form = OrderCreateForm(initial={'customer': order_customer, 'address': customer_address})

        # order = Order.objects.get_or_create(customer=order_customer, address=order_customer.location)
        return render(request, 'orders/create_order.html', {'form': form})


def pay_order(request):
    return render(request, 'shopping_cart/checkout.html')


def created_order(request):

    # cart = Cart(request)
    user_pk = request.user.pk
    order_customer = Profile.objects.get(user_id=user_pk)
    order_number = Order.objects.filter(customer=order_customer).last()
    # customer_address = Location.objects.get(pk=order_customer.location_id)
    context = {'order_number': order_number}

    return render(request, 'orders/created_order.html', context)
