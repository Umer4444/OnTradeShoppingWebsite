from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'myapp/home.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product_images = ProductImage.objects.filter(product=product)
    return render(request, 'myapp/product_detail.html', {'product': product, 'product_images': product_images})