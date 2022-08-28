from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title

    def add_amount(self):
        amount = self.product.price * self.quantity
        result = amount
        return result

    def save(self, *args, **kwargs):
        self.total_price = self.add_amount()
        return super(CartItem, self).save(*args, **kwargs)


