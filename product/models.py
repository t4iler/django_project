from django.db import models
from category.models import Category
from django.contrib.auth import get_user_model


User = get_user_model()

class Product(models.Model):
    '''
    Model for Product
    '''
    owner = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE, blank=False)
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    preview = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return f'{self.owner} - {self.title}'

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductImages(models.Model):
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')