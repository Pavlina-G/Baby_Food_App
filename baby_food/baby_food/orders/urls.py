from django.urls import path


from baby_food.orders.views import create_order, orders_list, pay_order, order_details, delete_order

urlpatterns = (
    path('create/', create_order, name='create order'),
    path('pay/<int:order_pk>/', pay_order, name='pay order'),
    path('created/', orders_list, name='orders list'),
    path('details/<int:pk>/', order_details, name='order details'),
    path('delete/<int:pk>/', delete_order, name='delete order'),
)