from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import Category
from . import serializers


class CategoryViewSet(ModelViewSet):
    queryset =  Category.objects.all()
    permission_classes = (permissions.IsAdminUser,)

    def get_serializer_class(self):
        return serializers.CategoryListSerializer
