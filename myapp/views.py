from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse


# Create your views here.

def home(request):
    products = Product.objects.all()
    products_baby = Product.objects.filter(category='Baby')[:4]  
    products_diy_tools = Product.objects.filter(category='DIY & Tools')[:4]  
    context = {
        'products': products,
        'products_baby': products_baby,
        'products_diy_tools': products_diy_tools,
    }
    return render(request, 'myapp/home.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product_images = ProductImage.objects.filter(product=product)
    category_products = Product.objects.filter(category=product.category)[:8]
    return render(request, 'myapp/product_detail.html', {'product': product, 'product_images': product_images, 'category_products': category_products})

def category_products(request, category):
    products = Product.objects.filter(category=category)
    return render(request, 'myapp/category_products.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    
    return redirect('cart_view')

def cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    
    if cart:
        products_in_cart = cart.products.all()
        total_products_in_cart = products_in_cart.count()

        # Calculate total price
        total_price = sum(product.price for product in products_in_cart)
    else:
        products_in_cart = []
        total_products_in_cart = 0
        total_price = 0  # No products in cart, so total price is zero

    return render(request, 'myapp/cart.html', {
        'products_in_cart': products_in_cart,
        'total_products_in_cart': total_products_in_cart,
        'total_price': total_price
    })

def get_cart_details(request):
    # Logic to fetch total_products and total_price from the cart
    cart, _ = Cart.objects.get_or_create(user=request.user)
    
    if cart:
        products_in_cart = cart.products.all()
        total_products = products_in_cart.count()

        # Calculate total price
        total_price = sum(product.price for product in products_in_cart)
    else:
        total_products = 0
        total_price = 0

    data = {
        'total_products': total_products,
        'total_price': total_price,
    }
    return JsonResponse(data)