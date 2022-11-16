from django.urls import path

from baby_food.menu_app.views import index, menus

urlpatterns = (
    path('', index, name='index'),
    path('menus/', menus, name='menus'),
)