import re
from datetime import datetime


from django.core import validators
from django.db import models

from baby_food.accounts.models import Profile, Child
from baby_food.common.models import Location

from baby_food.menu_app.models import Menu


class Order(models.Model):

    customer = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    paid = models.BooleanField(
        default=False,
    )
    address = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.customer} - cart_id: {self.id}'



class OrderItem(models.Model):
    MIN_PRICE = 0.00
    CURRENT_PRICE = 3.50

    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    product = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        default=1,
    )
    price = models.FloatField(
        default=CURRENT_PRICE,
        validators=(
            validators.MinValueValidator(MIN_PRICE),
        )
    )
    # address = models.ForeignKey(
    #     Location,
    #     on_delete=models.CASCADE
    # )

    address = models.CharField(
        max_length=200,
    )

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

