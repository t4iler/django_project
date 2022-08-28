from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from rating.serializers import ReviewSerializer
from . import serializers
from .models import Product, Favorites
from .permissions import IsAuthor



class StandartResultPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page'
    max_page_size = 1000


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = ('category', 'owner',)
    search_fields = ('title',)
    pagination_class = StandartResultPagination


    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductListSerializer
        elif self.action in ('create', 'update', 'partial_update'):
            return serializers.ProductCreateSerializer
        return serializers.ProductDetailSerializer


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)        # автоматически заполняет поле owner_id


    def get_permissions(self):
        
        # Создавать посты может зарегистрированный юзер
        if self.action in ('create', 'reviews', 'favorites'):
            return [permissions.IsAuthenticated()]

        # Изменять и удалять может только автор поста
        elif self.action in ('update', 'partial_update', 'destroy',):
            return [permissions.IsAuthenticated(), IsAuthor()]
        # Просматривать могут все
        else:
            return [permissions.AllowAny()]

    # api/v1/products/<id>/reviews/
    @action(['GET', 'POST'], detail=True)
    def reviews(self, request, pk=None):
        product = self.get_object()
        if request.method == 'GET':
            reviews = product.reviews.all()
            serializer = ReviewSerializer(reviews, many=True).data
            return Response(serializer, status=200)
        data = request.data
        serializer = ReviewSerializer(data=data, context={'request': request, 'product': product})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


        # api/v1/products/<id>/favorites
    @action(['POST'], detail=True) #если не указывать "detail=True", "pk" не нужен
    def favorites(self, request, pk):
        product = self.get_object()
        if request.user.favorites.filter(product=product).exists():
            request.user.favorites.filter(product=product).delete()
            return Response('Removed product from favorites!', status=204)
        Favorites.objects.create(product=product, owner=request.user) 
        return Response('Product added to favorites!', status=201)
