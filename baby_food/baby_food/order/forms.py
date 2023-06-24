from django import forms
from django.http import HttpRequest

from baby_food.accounts.models import Profile
from baby_food.order.models import Order, OrderItem


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order

        fields = ('customer', 'address')
        
        

        # widgets = {
        #     'customer': forms.TextInput(
        #         attrs={
        #             'readonly': 'readonly',
        #         }
        #     ),
        #     'address': forms.TextInput(
        #         attrs={
        #             'readonly': 'readonly',
        #         }
        #     )
        # }





