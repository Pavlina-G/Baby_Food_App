from django.db import models

from baby_food.common.models import Category


class Recipe(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='recipe_category'
    )

    name = models.CharField(
        max_length=50,
        unique=True,
    )

    dish_type = models.CharField(
        max_length=25,
        choices=(
            ('SOUP', 'SOUP'),
            ('MAIN DISH', 'MAIN DISH'),
            ('DESSERT', 'DESSERT'),
            ('Allergy-Free SOUP', 'Allergy-Free SOUP'),
            ('Allergy-Free MAIN DISH', 'Allergy-Free MAIN DISH'),
            ('Allergy-Free DESSERT', 'Allergy-Free DESSERT'),
        ),
    )

    ingredients = models.CharField(
        max_length=300,
    )

    weight = models.PositiveIntegerField(
        default=200,
        editable=False,
        blank=True,
    )

    def __str__(self):
        return f'{self.dish_type}: {self.name}'

