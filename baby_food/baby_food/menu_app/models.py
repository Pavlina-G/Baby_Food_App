from django.db import models

from baby_food.recipes.models import Recipe, RecipeWithoutAllergens


class BaseMenu(models.Model):
    class Meta:
        abstract = True

    date = models.DateField(
    )
    age = models.CharField(
        max_length=10,
        choices=(
            ('10M-18M', '10M-18M'),
            ('18M-36M', '18M-36M'),
        ),
    )
    soup = models.ForeignKey(
        Recipe,
        on_delete=models.DO_NOTHING,
        related_name='menu_soup',
    )
    main_dish = models.ForeignKey(
        Recipe,
        on_delete=models.DO_NOTHING,
        related_name='menu_main_dish',
    )
    dessert = models.ForeignKey(
        Recipe,
        on_delete=models.DO_NOTHING,
        related_name='menu_dessert',
    )
    price = models.PositiveIntegerField(
        default=3.00,
        editable=False,
    )
    quantity = models.PositiveIntegerField(
        default=1,
    )

class Menu(BaseMenu):
    pass


class MenuWithoutAllergens(BaseMenu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    age = models.CharField(
        max_length=10,
        choices=(
            ('10M-36M', '10M-36M'),
        ),
    )

    soup = models.ForeignKey(
        RecipeWithoutAllergens,
        on_delete=models.DO_NOTHING,
        related_name='menu_wa_soup',
    )
    main_dish = models.ForeignKey(
        RecipeWithoutAllergens,
        on_delete=models.DO_NOTHING,
        related_name='menu_wa_main_dish',
    )
    dessert = models.ForeignKey(
        RecipeWithoutAllergens,
        on_delete=models.DO_NOTHING,
        related_name='menu_wa_dessert',
    )

    class Meta:
        verbose_name_plural = 'Menu Without Allergens'
