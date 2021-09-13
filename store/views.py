from django.shortcuts import render, get_object_or_404
from .models import Producto
from categoria.models import Categoria
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.


def store(request, slug_categoria=None):

    categorias = None
    productos = None

    if slug_categoria != None:
        categorias = get_object_or_404(Categoria, slug=slug_categoria)
        productos = Producto.objects.filter(
            categoria=categorias, is_available=True)
        paginator = Paginator(productos, 3)
        page = request.GET.get('page')
        page_products = paginator.get_page(page)
        productos_contados = productos.count()
    else:
        productos = Producto.objects.all().filter(is_available=True)
        paginator = Paginator(productos, 6)
        page = request.GET.get('page')
        page_products = paginator.get_page(page)

        productos_contados = productos.count()

    context = {'productos': page_products,
               'productos_contados': productos_contados}
    return render(request, 'store/store.html', context)


def detalle_producto(request, slug_categoria, slug_producto):
    try:
        un_producto = Producto.objects.get(
            categoria__slug=slug_categoria, slug_producto=slug_producto)
        en_carrito = CartItem.objects.filter(
            cart__cart_id=_cart_id(request), producto=un_producto).exists()
    except Exception as e:
        raise e

    context = {'un_producto': un_producto, 'en_carrito': en_carrito}
    return render(request, 'store/producto_detalle.html', context)
