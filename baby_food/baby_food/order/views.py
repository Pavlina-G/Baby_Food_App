import random

from django import forms

from django.shortcuts import render, redirect
from django.urls import reverse
from multi_form_view import MultiModelFormView
from django.views import generic as views

from baby_food.accounts.models import Profile
from baby_food.common.models import Location
from baby_food.order.forms import OrderCreateForm, OrderPayForm
from baby_food.order.models import OrderItem, Order, Payments
from baby_food.shopping_cart.cart import Cart


def create_order(request):
    cart = Cart(request)
    user_pk = request.user.pk
    order_customer = Profile.objects.get(user_id=user_pk)
    customer_address = Location.objects.get(pk=order_customer.location_id)
    total_amount = cart.get_total_price()

    if request.method == 'POST':

        form = OrderCreateForm(request.POST, initial={'customer': order_customer, 'address': customer_address,
                                                      'order_amount': total_amount})

        if form.is_valid():

            order = form.save(commit=False)
            order.customer = order_customer
            order.address = customer_address
            order.order_amount = total_amount

            order.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['menu'],
                    price=item['price'],
                    quantity=item['quantity'],
                    address=item['location']
                )

            # cart.clear()

            return redirect('pay order')

        # to add error message

        return render(request, 'orders/create_order.html', {'form': form})
    else:
        form = OrderCreateForm(
            initial={'customer': order_customer, 'address': customer_address, 'order_amount': total_amount}
        )

        return render(request, 'orders/create_order.html', {'form': form})


def pay_order(request):
    user_pk = request.user.pk
    customer = Profile.objects.get(user_id=user_pk)
    order = Order.objects.filter(customer=customer).last()
    cart = Cart(request)

    if request.method == 'POST':
        payment_form = OrderPayForm(request.POST)

        if payment_form.is_valid():
            payments = payment_form.save(commit=False)

            payments.order_id = order
            payments.payment_number = order.payment_ref_number
            payments.save()

            order.paid = True
            order.save()

            cart.clear()

            return redirect('created order')
        else:

            return render(request, 'shopping_cart/checkout.html', {'payment_form': payment_form})

    else:
        payment_form = OrderPayForm(request.POST)

        return render(request, 'shopping_cart/checkout.html', {'payment_form': payment_form})


# Order details view - to add
def created_order(request):
    # cart = Cart(request)
    user_pk = request.user.pk
    order_customer = Profile.objects.get(user_id=user_pk)
    order_number = Order.objects.filter(customer=order_customer).last()
    # customer_address = Location.objects.get(pk=order_customer.location_id)
    context = {'order_number': order_number}

    return render(request, 'orders/created_order.html', context)
