from django.urls import path

from baby_food.cart.views import cart_details

urlpatterns = (
    path('cart/', cart_details, name='cart details'),
)