from .models import Cart, CartItem
from .views import _cart_id


def contador_carrito(request):
    contador = 0

    try:
        cart = Cart.objects.filter(cart_id=_cart_id(request))
        cart_items = CartItem.objects.all().filter(cart=cart[:1])

        for cart_item in cart_items:
            contador += cart_item.quantity

    except Cart.DoesNotExist:
        contador = 0

    return dict(contador=contador)
