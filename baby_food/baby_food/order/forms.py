
import random
from datetime import datetime

from django import forms
from django.http import HttpRequest


from baby_food.accounts.models import Profile
from baby_food.order.models import Order, OrderItem, Payments


def create_new_payment_number():
    return str(random.randint(100000000000, 999999999999))


class OrderCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.fields['customer'].disabled = True
        self.fields['customer'].widget.attrs.update({"class": 'checkout-card-form-input'})
        self.fields['address'].disabled = True
        self.fields['address'].widget.attrs.update({"class": 'checkout-card-form-input'})

    class Meta:
        model = Order

        fields = ('customer', 'address',)


class OrderPayForm(forms.ModelForm):

    class Meta:
        model = Payments

        YEAR_CHOICES = [(y, y) for y in range(2023, datetime.now().year + 7)]
        MONTH_CHOICE = [(m, m) for m in range(1, 13)]

        exclude = ('payment_number', 'order_id')

        widgets = {
            'card_holder': forms.TextInput(
                attrs={
                    'placeholder': 'Enter card holder name',
                    'class': 'checkout-card-form-input',

                }
            ),
            'card_number': forms.NumberInput(
                attrs={
                    'class': 'checkout-card-form-input',
                    'placeholder': "Enter your card number",
                    'id': "cardNumId",
                    'required': True,
                    # 'type': 'text',
                }
            ),
            'card_expiry_month': forms.Select(
                choices=MONTH_CHOICE,
                attrs={
                    'class': 'checkout-card-form-input exp ccv-label',
                    'placeholder': 'MM',
                    'style': 'width:18%',
                },
            ),

            'card_expiry_year': forms.Select(
                choices=YEAR_CHOICES,
                attrs={
                    'class': 'checkout-card-form-input exp ccv-label',
                    'placeholder': 'YY',
                }
            ),
            'card_verification_code': forms.PasswordInput(
                attrs={
                    'class': 'checkout-card-form-input exp',
                    'placeholder': '123',
                    # 'type': 'number',
                }
            ),

        }
