from django.contrib import admin
from .models import *

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        # Retrieve the products related to the cart being deleted
        products = obj.products.all()
        
        # Remove the association of these products with the cart
        for product in products:
            obj.products.remove(product)

        # Continue with the deletion of the cart
        super().delete_model(request, obj)


