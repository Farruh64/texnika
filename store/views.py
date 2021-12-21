from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render,get_object_or_404
from store.models import  *
from cart.views import _cart_id
from cart.models import *

def store(request, category_slug = None):

    if category_slug == None:
        products = Product.objects.filter(is_available = True)
    else:
        categories = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(is_available = True, category = categories)
    
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products': paged_products,
        'product_count': products.count()
    }
    return render(request, 'store.html',context)

def product_detail(request, category_slug,product_slug):
    product = get_object_or_404(Product, slug = product_slug, category__slug=category_slug)
    cart_in = CartItem.objects.filter(cart__session_id = _cart_id(request), product = product).exists
    context = {
        'product':product,
        'cart_in':cart_in
    }
    return render(request, 'products_detail.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
    if keyword:
        products = Product.objects.filter(Q(name__icontains=keyword) | Q(description__icontains=keyword))
    
    context = {
        'products': products,
        'product_count': products.count()
    }
    return render(request, 'store.html', context)    
# Create your views here.
