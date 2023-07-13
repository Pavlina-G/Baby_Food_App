from totalsum.admin import TotalsumAdmin

from django.contrib import admin
from baby_food.order.models import Order,OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


class CategoryListFilter(admin.SimpleListFilter):
    title = 'menu category'

    parameter_name = 'category'

    def lookups(self, request, model_admin):
        return [
            ('Allergy Free', 'Allergy Free'),
            ('With Allergens', 'With Allergens')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'Allergy Free':
            return queryset.filter(product__category=1).order_by('-product')
        elif self.value() == 'With Allergens':
            return queryset.filter(product__category=2).order_by('-product')


@admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
class OrderItemAdmin(TotalsumAdmin):

    list_display = ('product', 'quantity', 'total_price', 'address', 'get_menu_date', 'order')
    list_filter = ('product', 'order', CategoryListFilter, 'address',)

    search_fields = ('product__date', 'address__city', 'address__address', 'product__category__category_name')

    totalsum_list = ('quantity', 'total_price')

    def total_price(self, obj):
        return obj.price * obj.quantity

    def get_menu_date(self, obj):
        return obj.product.date

    get_menu_date.admin_order_field = '-product__date'
    get_menu_date.short_description = 'menu_date'
