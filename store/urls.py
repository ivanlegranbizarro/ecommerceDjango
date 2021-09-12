from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:slug_categoria>/', views.store, name='products_by_category'),
    path('<slug:slug_categoria>/<slug:slug_producto>',
         views.detalle_producto, name='detalle_producto'),
]
