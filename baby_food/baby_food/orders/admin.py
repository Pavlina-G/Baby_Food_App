from totalsum.admin import TotalsumAdmin

from django.contrib import admin
from baby_food.orders.models import Order, OrderItem, Payments


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'address', 'order_amount', 'total_paid',)
    list_filter = ('paid', 'address')

    search_fields = (
        'address__address', 'customer__first_name', 'customer__last_name', 'customer__user__username', 'pk')

    def total_paid(self, obj):
        if obj.paid:
            return obj.order_amount


@admin.register(OrderItem)
class OrderItemAdmin(TotalsumAdmin):
    list_display = ('product', 'quantity', 'total_price', 'address', 'get_menu_date', 'order',)
    list_filter = ('product', 'order', 'product__category', 'address',)

    search_fields = (
        'product__date', 'address', 'order__pk', 'order__customer__first_name', 'order__customer__last_name',
        'product__category__category_name', 'order__customer__user__username')

    totalsum_list = ('quantity', 'total_price')

    def total_price(self, obj):
        return obj.price * obj.quantity

    def get_menu_date(self, obj):
        return obj.product.date

    get_menu_date.admin_order_field = '-product__date'
    get_menu_date.short_description = 'menu_date'


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'payment_number', 'payment_date')
    list_filter = ('payment_date',)
    exclude = ('card_verification_code', 'payment_date')
    readonly_fields = ('payment_date',)

    fieldsets = (
        (
            'Payment info',
            {
                'fields': (
                    'order_id',
                    'payment_number',
                    'payment_date',
                ),
            },
        ),
    )
