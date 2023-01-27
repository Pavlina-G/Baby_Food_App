from django.contrib import admin

from baby_food.recipes.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'dish_type', 'category',)
    list_filter = ('dish_type', 'category',)

    def get_allergy_free_recipes(self):
        return self.objects.filter(category_id=1)
