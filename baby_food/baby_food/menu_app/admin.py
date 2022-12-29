from django.contrib import admin

from baby_food.menu_app.models import Menu, MenuWithoutAllergens


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('date', 'age', 'soup', 'main_dish', 'dessert')
    list_filter = ('age', 'date',)


@admin.register(MenuWithoutAllergens)
class MenuWithoutAllergensAdmin(admin.ModelAdmin):
    list_display = ('date', 'age', 'soup', 'main_dish', 'dessert')
    list_filter = ('age', 'date',)

