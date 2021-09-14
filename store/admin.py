from django.contrib import admin
from .models import Producto, Variation

# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto', 'precio',
                    'categoria', 'modified_date', 'is_available']
    prepopulated_fields = {'slug_producto': ['nombre_producto', ]}


class VariationAdmin(admin.ModelAdmin):
    list_display = ('producto', 'categoria_variacion',
                    'is_active', 'valores_variacion')
    list_editable = ('is_active',)
    list_filter = ('producto', 'is_active',
                   'valores_variacion', 'categoria_variacion')


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Variation, VariationAdmin)
