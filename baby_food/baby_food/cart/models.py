import re
from datetime import datetime

from django.core import validators
from django.db import models
#
from baby_food.accounts.models import Profile, Child
from baby_food.common.models import Location
# from baby_food.common.models import Location
from baby_food.menu_app.models import Menu


class Cart(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        default=datetime.now
    )

    def __str__(self):
        return f'{self.user} - cart_id: {self.id}'



class CartItem(models.Model):
    MIN_PRICE = 0.00

    product = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        default=1,
    )
    price = models.FloatField(
        default=3.50,
        validators=(
            validators.MinValueValidator(MIN_PRICE),
        )
    )

    address = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
    )
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

    @property
    def total_price(self):
        return self.price * self.quantity

    @property
    def get_menu_date(self):
        return self.product.date

    @property
    def get_menu_category(self):
        return self.product.category

    def __str__(self):
        return f'{self.product} - Quantity: {self.quantity}'

    class Meta:
        ordering = ['-product__date']

