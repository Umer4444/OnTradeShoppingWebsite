from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('category/<str:category>/', views.category_products, name='category_products'),

]
