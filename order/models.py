from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save


from product.models import Product


User = get_user_model()


STATUS_CHOICES = (
    ('Open', 'Открыт'),
    ('In_process', 'В обработке'),
    ('Closed', 'Закрыт')
)



class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.RESTRICT)
    product = models.ManyToManyField(Product, through='OrderItem')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orders', on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.SmallIntegerField(default=1)


