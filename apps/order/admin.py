from django.contrib import admin
from apps.order import models as order_models


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'order_type')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_code', 'item_name')
    search_fields = ('item_code', 'item_name')
    ordering = ('item_code',)


class OrderCartItem(admin.ModelAdmin):
    list_display = ('order', 'item')
    search_fields = ('order', 'item')


admin.site.register(order_models.Order, OrderAdmin)
admin.site.register(order_models.Item, ItemAdmin)
admin.site.register(order_models.OrderCartItem, OrderCartItem)
