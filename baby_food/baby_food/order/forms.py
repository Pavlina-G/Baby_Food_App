from django import forms

from baby_food.order.models import Order, OrderItem


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user',)
