from django.contrib import admin

from baby_food.menu_app.models import Menu
from baby_food.recipes.models import Recipe


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('date', 'age', 'soup', 'main_dish', 'dessert', 'category')
    list_filter = ('age', 'date', 'category')
    search_fields = ('soup', 'main_dish', 'dessert')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "soup":
            kwargs["queryset"] = Recipe.objects.filter(dish_type__icontains='soup')
        if db_field.name == "dessert":
            kwargs["queryset"] = Recipe.objects.filter(dish_type__icontains='dessert')
        if db_field.name == "main_dish":
            kwargs["queryset"] = Recipe.objects.filter(dish_type__icontains='main dish')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
