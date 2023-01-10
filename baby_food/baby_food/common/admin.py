from django.contrib import admin

from baby_food.common.models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass
