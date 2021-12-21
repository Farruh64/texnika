from cart.models import CartItem ,Cart
from cart.views import _cart_id

def counter(request):
    try:
        cart = Cart.objects.get(session_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart = cart)

        count = 0
        for cart_item in cart_items:
            count += cart_item.quantity 
    except Cart.DoesNotExist:
        count = 0
    return dict(count = count)    