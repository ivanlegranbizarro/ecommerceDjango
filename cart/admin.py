from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'date_joined']


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['producto', 'cart', 'quantity', 'is_active', ]


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
