from django.urls import path

from baby_food.common.views import IndexView, locations_map, GalleryView

urlpatterns = (
    # path('', index, name='index')
    path('', IndexView.as_view(), name='index'),
    path('locations/', locations_map, name='locations map'),
    path('gallery/', GalleryView.as_view(), name='gallery pictures'),
)
