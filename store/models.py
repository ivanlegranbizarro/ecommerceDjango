from django.db import models
from categoria.models import Categoria
from django.urls import reverse

# Create your models here.


class Producto(models.Model):
    nombre_producto = models.CharField(max_length=200, unique=True)
    slug_producto = models.SlugField(max_length=200, unique=True)
    descripcion_producto = models.TextField(max_length=500, blank=True)
    precio = models.DecimalField(decimal_places=2, max_digits=5)
    imagen_producto = models.ImageField(upload_to='imagenes/productos')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('detalle_producto', args=(self.categoria.slug, self.slug_producto))

    def __str__(self):
        return self.nombre_producto


class Variation(models.Model):

    variaciones = (
        ('color', 'Color'),
        ('talla', 'Talla'),
    )

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    categoria_variacion = models.CharField(max_length=10, choices=variaciones)
    valores_variacion = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.producto.nombre_producto
