from django.db import models

from baby_food.common.models import Category
from baby_food.recipes.models import Recipe


class Menu(models.Model):
    date = models.DateField(
    )
    age = models.CharField(
        max_length=10,
        choices=(
            ('10M-18M', '10M-18M'),
            ('18M-36M', '18M-36M'),
            ('10M-36M', '10M-36M'),
        ),
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='menu_category'
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
        verbose_name='main dish',
    )
    dessert = models.ForeignKey(
        Recipe,
        on_delete=models.DO_NOTHING,
        related_name='menu_dessert',
    )

    price = models.PositiveIntegerField(
        default=3.50,
        editable=False,
    )

    def __str__(self):
        return f'Allergy-Free Menu: {self.date}' if self.category_id == 1 else f'Menu With Allergens: {self.date}'

    @staticmethod
    def get_menu_by_id(menu_id):
        return Menu.objects.filter(id=menu_id)

    @staticmethod
    def get_all_menus():
        return Menu.objects.all()

    @staticmethod
    def get_all_menus_by_category_id(category_id):
        if category_id:
            return Menu.objects.filter(category=category_id)
        else:
            return Menu.get_all_menus()
