from rest_framework import serializers
from .models import CartItem
from product import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()


class CartItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.email')
    product = serializers.ReadOnlyField(source='product.title')
    price = serializers.ReadOnlyField(source='product.price')

    class Meta:
        model = CartItem
        exclude = ('user',)


    
class CartItemAddSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.email')
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CartItem
        fields = ('id', 'owner','quantity', 'product_id', 'total_price', 'created_at')
        extra_kwargs = {
            'quantity': {'required': True},
            'product_id': {'required': True},
        }

    def create(self, validated_data):
        user = User.objects.get(id=self.context['request'].user.id)
        product = get_object_or_404(models.Product, id=validated_data['product_id'])
        if product.quantity == 0 or product.is_available is False:
            raise serializers.ValidationError(
                {'Not available': 'The product is not available.'})
        elif product.quantity < validated_data['quantity']:
            raise serializers.ValidationError(
                {'Not available': f'Total products at the moment:({product.quantity})!'})

        cart_item = CartItem.objects.create(
            product=product,
            user=user,
            quantity=validated_data['quantity']
            )
        cart_item.save()
        cart_item.add_amount()
        product.quantity -= cart_item.quantity
        product.save()
        return cart_item