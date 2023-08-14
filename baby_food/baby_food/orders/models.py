from datetime import datetime

from encrypted_fields import fields

from django.db import models

from baby_food.accounts.models import Profile, Child
from baby_food.common.models import Location
from baby_food.common import validators as my_validators
from django.core import validators

from baby_food.menus.models import Menu


def create_new_payment_number(pk):
    return str(datetime.now().date()) + '-' + str(pk)


class Order(models.Model):
    customer = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    address = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    order_amount = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        error_messages={
            "wrong amount": "The orders amount must be more than 3 BGN",
        },
        blank=True,
    )

    paid = models.BooleanField(
        default=False,
    )

    @property
    def payment_ref_number(self):
        return f"{self.customer.user_id}-{self.customer.user.username.upper()[0]}-{create_new_payment_number(self.pk)}"

    def __str__(self):
        return f'{self.customer} - cart_id: {self.pk}'


class OrderItem(models.Model):
    MIN_PRICE = 0.00
    CURRENT_PRICE = 3.50

    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    product = models.ForeignKey(
        Menu,
        on_delete=models.DO_NOTHING
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


class Payments(models.Model):
    YEAR_CHOICES = [(y, y) for y in range(datetime.now().year, datetime.now().year + 5)]
    MONTH_CHOICE = [(m, m) for m in range(1, 13)]

    order_id = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    payment_number = models.CharField(
        validators=[validators.MinLengthValidator(12), validators.MaxLengthValidator(12)],
        blank=False,
        null=False,
        max_length=80,
        unique=True,
    )

    card_holder = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        validators=[my_validators.validate_name]
    )

    card_number = models.PositiveBigIntegerField(
        blank=False,
        null=False,
        validators=[
            my_validators.validate_card_number,
        ]
    )

    card_expiry_year = models.IntegerField(
        choices=YEAR_CHOICES,
        validators=[validators.MinValueValidator(datetime.now().year),
                    validators.MaxValueValidator(datetime.now().year + 5),
                    ]
    )

    card_expiry_month = models.IntegerField(
        choices=MONTH_CHOICE,
    )

    card_verification_code = fields.EncryptedPositiveIntegerField(
        validators=[validators.MinValueValidator(000), validators.MaxValueValidator(999),
                    ],
    )

    payment_date = models.DateField(
        auto_now_add=True,

    )

    def __str__(self):
        return f'Payment No. {self.payment_number}'

    class Meta:
        verbose_name_plural = 'Payments'

        ordering = ['-payment_date']
