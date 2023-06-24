from django.contrib.auth.decorators import login_required
from django.urls import path

from baby_food.shopping_cart.views import cart_details, add_to_cart, remove_from_cart

urlpatterns = (
    path('add-<int:pk>/', login_required(add_to_cart), name='add to cart'),
    path('remove-<int:pk>/', login_required(remove_from_cart), name='remove from cart'),
    path('details/', login_required(cart_details), name='cart details'),
)