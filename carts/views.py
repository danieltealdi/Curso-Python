from django.shortcuts import render, redirect, get_object_or_404

from carts.funciones import funcionCarrito
from carts.models import CartProduct, CartProductManager
from products.models import Product


def cart(request):
    cart=funcionCarrito(request)
    return render(request, 'carts/cart.html', {'cart':cart})

def add(request):
    cart = funcionCarrito(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    quantity=int(request.POST.get('quantity', 1))
    #cart.products.add(product, through_defaults={'quantity':quantity})
    product_cart = CartProduct.object.crearActualizar(cart=cart, product=product, quantity=quantity)
    return render(request, 'carts/add.html', {"product":product})
def remove(request):
    cart = funcionCarrito(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))
    cart.products.remove(product)
    return redirect('cart')
