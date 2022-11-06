from django.db import models


class BaseRecipe(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(
        max_length=50,
    )
    dish_type = models.CharField(
        max_length=10,
        choices=(
            ('SOUP', 'SOUP'),
            ('MAIN_DISH', 'MAIN_DISH'),
            ('DESSERT', 'DESSERT'),
        ),
    )
    allergens = models.CharField(
        max_length=3,
        default='YES',
        editable=False,
    )
    ingredients = models.CharField(
        max_length=300,
    )

    weight = models.PositiveIntegerField(
        default=200,
        editable=False,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.dish_type}: {self.name}'


class Recipe(BaseRecipe):
    pass


class RecipeWithoutAllergens(BaseRecipe):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, kwargs)

        allergens = models.CharField(
            max_length=2,
            default='NO',
            editable=False,
        )

    class Meta:
        verbose_name_plural = 'Recipes Without Allergens'
