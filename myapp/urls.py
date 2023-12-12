from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('category/<str:category>/', views.category_products, name='category_products'),
    path('cart/', views.cart_view, name='cart_view'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('get_cart_details/', views.get_cart_details, name='get_cart_details'),

]
