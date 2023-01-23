from django.db import models

from baby_food.accounts.models import Profile, Child
from baby_food.common.models import Location
from baby_food.menu_app.models import Menu, MenuWithoutAllergens


class Order(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    child_id = models.PositiveIntegerField(
        unique=True,
    )

    menu_type = models.CharField(
        max_length=150,
        choices=(
            ('Allergy-Free', 'Allergy-Free'),
            ('With Allergens', 'With Allergens'),
        )
    )

    allergy_free_menu = models.ForeignKey(
        MenuWithoutAllergens,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    allergy_menu = models.ForeignKey(
        Menu,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    menu_date = models.DateField()

    age_range = models.CharField(
        max_length=30,
        choices=(
            ('10M-36M Allergy-Free', '10M-36M Allergy-Free'),
            ('10M-18M', '10M-18M'),
            ('18M-36M', '18M-36M'),
        ),
        blank=True,
        null=True,
    )
    quantity = models.PositiveIntegerField(
        default=1,
    )
    price = models.FloatField(
        default=3.50,
    )

    address = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
    )
    created_on = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'User: {self.user.first_name} {self.user.last_name}, Menu: {self.menu_type}, Date: {self.menu_date} Age: {self.age_range}'
