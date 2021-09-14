from django.shortcuts import render, redirect, get_object_or_404
from store.models import Producto, Variation
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    variaciones_producto = []

    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]

            try:
                variaciones = Variation.objects.get(
                    producto=producto, categoria_variacion__iexact=key,
                    valores_variacion__iexact=value)
                variaciones_producto.append(variaciones)
            except:
                pass

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
    cart.save()

    try:
        cart_item = CartItem.objects.get(producto=producto, cart=cart)
        if len(variaciones_producto) > 0:
            cart_item.variaciones.clear()
            for item in variaciones_producto:
                cart_item.variaciones.add(item)

        cart_item.quantity += 1
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            producto=producto, quantity=1, cart=cart,)

        if len(variaciones_producto) > 0:
            cart_item.variaciones.add(item)
        cart_item.save()

    return redirect('cart')


def remove_cart(request, producto_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    producto = get_object_or_404(Producto, id=producto_id)
    cart_item = CartItem.objects.get(producto=producto, cart=cart)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')


def remove_cart_item(request, producto_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    producto = get_object_or_404(Producto, id=producto_id)
    cart_item = CartItem.objects.get(producto=producto, cart=cart)

    cart_item.delete()

    return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=None):

    tax = 0
    grand_total = 0

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.producto.precio * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (total*2)/100
        grand_total = total + tax

    except ObjectDoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }

    return render(request, 'store/cart.html', context)
