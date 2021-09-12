from django.db import models
from django.urls import reverse

# Create your models here.


class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    cat_imagen = models.ImageField(upload_to='imagenes/categorias', blank=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.nombre_categoria
