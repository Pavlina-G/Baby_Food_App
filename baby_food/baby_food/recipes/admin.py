from django.contrib import admin

from baby_food.recipes.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'dish_type', 'category',)
    list_filter = ('dish_type', 'category', 'added_on')
    search_fields = ('name', )

