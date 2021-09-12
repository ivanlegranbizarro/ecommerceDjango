from django.contrib import admin
from .models import Producto

# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto', 'precio',
                    'categoria', 'modified_date', 'is_available']
    prepopulated_fields = {'slug_producto': ['nombre_producto', ]}


admin.site.register(Producto, ProductoAdmin)
