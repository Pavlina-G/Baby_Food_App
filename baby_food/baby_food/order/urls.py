from django.urls import path

from baby_food.order.views import create_order, created_order, pay_order, order_details, delete_order

urlpatterns = (
    # path('create/', create_order, name='create order'),
    path('create/', create_order, name='create order'),
    path('pay/<int:order_pk>/', pay_order, name='pay order'),
    # path('pay/order-<int:pk>/', pay_order, name='pay order'),
    path('created/', created_order, name='created order'),
    path('details/<int:pk>/', order_details, name='order details'),
    path('delete/<int:pk>/', delete_order, name='delete order'),
)