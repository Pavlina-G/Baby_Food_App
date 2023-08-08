from django.contrib import admin

from baby_food.common.models import Gallery, Location, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('picture', 'upload_date')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
