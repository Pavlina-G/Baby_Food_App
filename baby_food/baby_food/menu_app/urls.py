from django.urls import path

from baby_food.menu_app.views import index

urlpatterns = (
    path('', index, name='index'),
)