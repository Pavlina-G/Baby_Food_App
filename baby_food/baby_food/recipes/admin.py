from django.contrib import admin

from baby_food.recipes.models import Recipe, RecipeWithoutAllergens


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'dish_type')
    list_filter = ('dish_type',)


@admin.register(RecipeWithoutAllergens)
class RecipeWithoutAllergens(admin.ModelAdmin):
    list_display = ('name', 'dish_type')
    list_filter = ('dish_type',)



