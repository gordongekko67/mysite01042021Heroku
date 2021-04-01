from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.http import HttpResponse, JsonResponse
import  os

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],'override': True})
    
    return render(request, 'cart/detail.html', {'cart': cart})


def prova_django(request):
    msg = f'prova visualizzazione dati django  da cart '
    return HttpResponse(msg, content_type='text/plain')


def homecart(request):
    return render(request, "pippo.html")