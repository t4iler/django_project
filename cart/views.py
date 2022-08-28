from rest_framework import permissions, filters, generics, response

from django.shortcuts import get_object_or_404
from .serializers import CartItemSerializer, CartItemAddSerializer, CartItem
from .models import Product



class CartItemView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['product__name', 'product__description', 'product__category__name']

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(user=user)



class CartItemAddView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemAddSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CartItemDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CartItem.objects.all()


    def delete(self, request, pk, format=None):
        user = request.user
        cart_item = CartItem.objects.filter(user=user)
        target_product = get_object_or_404(cart_item, pk=pk)
        product = get_object_or_404(Product, id=target_product.product.id)
        product.quantity = product.quantity + target_product.quantity
        product.save()
        target_product.delete()
        return response.Response(data={"detail": "deleted"}, status=200)

