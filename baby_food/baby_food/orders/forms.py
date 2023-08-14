import random
from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from baby_food.orders.models import Order, Payments


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

    def clean(self):
        cleaned_data = super(OrderPayForm, self).clean()
        month = cleaned_data.get('card_expiry_month')
        year = cleaned_data.get('card_expiry_year')

        if year == datetime.now().year and month < datetime.now().month:
            self.add_error('card_expiry_month', ValidationError("The month is not valid!"))

        return cleaned_data

    class Meta:
        model = Payments

        MONTH_CHOICES = [(m, m) for m in range(1, 13)]

        exclude = ('payment_number', 'order_id', '')

        widgets = {
            'card_holder': forms.TextInput(
                attrs={
                    'placeholder': 'Enter card holder name',
                    'class': 'checkout-card-form-input',
                    'oninvalid': 'this.setCustomValidity("Enter a valid name.")',
                }
            ),

            'card_number': forms.NumberInput(
                attrs={
                    'class': 'checkout-card-form-input',
                    'placeholder': "Enter your card number",
                    'id': "cardNumId",
                    'oninvalid': 'this.setCustomValidity("The card number must contain 16 digits.")',
                }
            ),
            'card_expiry_month': forms.Select(
                attrs={
                    'class': 'checkout-card-form-input exp ccv-label',
                    'placeholder': 'MM',
                    'style': 'width:18%',
                    'oninvalid': 'this.setCustomValidity("The month is in the past.")',
                },
            ),
            'card_expiry_year': forms.Select(
                attrs={
                    'class': 'checkout-card-form-input exp ccv-label',
                    'placeholder': 'YYYY',
                }
            ),
            'card_verification_code': forms.PasswordInput(
                attrs={
                    'class': 'checkout-card-form-input exp',
                    'placeholder': '123',
                }
            ),

        }
