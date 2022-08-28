from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model

from account import serializers

from .serializers import ProfileListSerializer, ProfileDetailSerializer

User = get_user_model()

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ProfileListSerializer
        elif self.action in ('create', 'update', 'partial_update'):
            return serializers.RegisterSerializer
        return ProfileDetailSerializer


    def get_permissions(self):
        if self.action in ('create',):
            return (permissions.AllowAny(),)
        # смотреть посты может зарегистрированный юзер
        elif self.action in ('reviews',):
            return (permissions.IsAuthenticated(),)

        # Изменять и удалять может только автор поста
        elif self.action in ('update', 'partial_update'):
            return (permissions.IsAdminUser,)
        # Просматривать могут все
        else:
            return [permissions.AllowAny()]

