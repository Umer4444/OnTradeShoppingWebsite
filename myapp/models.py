from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    CATEGORY = (
        ('Baby', 'Baby'),
        ('DIY & Tools', 'DIY & Tools'),
        ('Grocery', 'Grocery'),
        ('Health & Beauty', 'Health & Beauty'),
        ('Home & Kitchen', 'Home & Kitchen'),
        ('Office Products', 'Office Products'),
        ('Pet Supplies', 'Pet Supplies'),
        ('Sports & Outdoors', 'Sports & Outdoors'),
        ('Toys', 'Toys'),
    )
    title = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    short_description = models.CharField(max_length=255, null=True, blank=True)
    detailed_description = models.TextField()

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.title}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product')