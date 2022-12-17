from django.urls import path

from baby_food.menu_app.views import menus_home, menus_no_allergens, menus_with_allergens

urlpatterns = (
    path('', menus_home, name='menus home'),
    path('with-allergens/', menus_with_allergens, name='menus with allergens'),
    path('no-allergens/', menus_no_allergens, name='menus no allergens'),
)