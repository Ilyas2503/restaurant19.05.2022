from django.contrib import admin

from .models import Table, Menu, OrderItem, Order

admin.site.register(Table)
admin.site.register(Menu)
admin.site.register(OrderItem)
admin.site.register(Order)
# Register your models here.
