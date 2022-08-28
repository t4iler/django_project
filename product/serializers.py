from xml.etree.ElementInclude import include
from rest_framework import serializers
from django.db.models import Avg

from .models import Product, ProductImages, Favorites



class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        exclude = ('id',)


class ProductListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    

    class Meta:
        model = Product
        fields = ('id', 'owner', 'title', 'description', 'category', 'price', 'preview', 'created_at')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        return repr

class ProductDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        repr['reviews_count'] = instance.reviews.count()
        return repr

class ProductCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    images = ProductImageSerializer(many=True, read_only=False, required=False)


    class Meta:
        model = Product
        fields = ('owner', 'title', 'description', 'category', 'price', 'quantity', 'preview', 'images',)

    def create(self, validated_data):
        request = self.context.get('request')
        created_product = Product.objects.create(**validated_data)
        images_data = request.FILES
        images_object = [ProductImages(product=created_product, image=image) for image in images_data.getlist('images')]
        ProductImages.objects.bulk_create(images_object)
        return created_product

        
    

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = '__all__'
    
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['product'] = ProductListSerializer(instance.product).data
        return repr