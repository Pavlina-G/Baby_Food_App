from django.urls import path

from baby_food.menu_app.views import menu_home, menu_no_allergens, menu_with_allergens_last, menu_with_allergens_first

urlpatterns = (
    path('', menu_home, name='menus home'),
    path('with-allergens-18/', menu_with_allergens_first, name='menu with allergens 18M'),
    path('with-allergens-36/', menu_with_allergens_last, name='menu with allergens 36M'),
    path('no-allergens/', menu_no_allergens, name='menu_app no allergens'),
)