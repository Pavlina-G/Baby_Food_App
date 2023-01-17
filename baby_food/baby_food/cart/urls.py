from django.urls import path

from baby_food.cart.views import cart_details

urlpatterns = (
    path('shopping-cart/', cart_details, name='cart details'),
)