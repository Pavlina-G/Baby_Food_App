from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404

from baby_food.accounts.models import Profile
from baby_food.common.models import Location
from baby_food.common.utils import is_staff
from baby_food.orders.forms import OrderCreateForm, OrderPayForm
from baby_food.orders.models import OrderItem, Order

from baby_food.shopping_cart.cart import Cart


@login_required
def create_order(request):

    cart = Cart(request)
    user_pk = request.user.pk
    order_customer = get_object_or_404(Profile, pk=user_pk)

    if is_staff(request):
        cart.clear()
        return redirect('profile home')

    if order_customer.child_set.all().count() == 0:
        cart.clear()
        return redirect('profile home')

    customer_address = get_object_or_404(Location, pk=order_customer.location_id)

    total_amount = cart.get_total_price()

    if request.method == 'POST':

        form = OrderCreateForm(request.POST, initial={'customer': order_customer, 'address': customer_address,
                                                      'order_amount': total_amount})

        if form.is_valid():

            order = form.save(commit=False)
            order.customer = order_customer
            order.address = customer_address
            order.order_amount = total_amount
            if order.order_amount > 0:
                order.save()

                for item in cart:
                    OrderItem.objects.create(
                        order=order,
                        product=item['menu'],
                        price=item['price'],
                        quantity=item['quantity'],
                        address=item['location']
                    )
                cart.clear()

                return redirect('pay order', order.id)
            else:
                return redirect('cart details')

        return render(request, 'orders/create_order.html', {'form': form})
    else:
        form = OrderCreateForm(
            initial={'customer': order_customer, 'address': customer_address, 'order_amount': total_amount}
        )

        return render(request, 'orders/create_order.html', {'form': form})


@login_required
def pay_order(request, order_pk):
    user_pk = request.user.pk
    customer = Profile.objects.get(user_id=user_pk)
    order = Order.objects.filter(customer=customer, pk=order_pk).last()

    if is_staff(request):
        return redirect('profile home')

    if request.method == 'POST':
        payment_form = OrderPayForm(request.POST)

        if payment_form.is_valid():
            payments = payment_form.save(commit=False)

            payments.order_id = order
            payments.payment_number = order.payment_ref_number

            payments.save()

            order.paid = True
            order.save()

            return redirect('orders list')
        return render(request, 'shopping_cart/checkout.html', {'payment_form': payment_form, 'order': order})

    else:
        payment_form = OrderPayForm()
        return render(request, 'shopping_cart/checkout.html', {'payment_form': payment_form, 'order': order})


@login_required
def orders_list(request):
    user_pk = request.user.pk
    order_customer = get_object_or_404(Profile, pk=user_pk)
    order = Order.objects.filter(customer=order_customer).last()
    orders = Order.objects.filter(customer=order_customer, ).order_by('-created_at')[:10]

    context = {'order': order, 'orders': orders}

    return render(request, 'orders/orders_list.html', context)


@login_required
def order_details(request, pk):
    order = Order.objects.get(pk=pk)
    order_items = order.orderitem_set.all()

    context = {'order_items': order_items, 'order': order}

    return render(request, 'orders/order-details.html', context)


@login_required
def delete_order(request, pk):
    order = Order.objects.get(pk=pk)

    order.delete()

    return redirect('orders list')
