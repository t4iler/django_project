from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileListSerializer(serializers.ModelSerializer):
    """
    serializer for user that serialize :
    ('id', 'email', 'image', 'is_active')
    based on default 'User' model
    """

    class Meta:
        model = User
        fields = ('id', 'email', 'image', 'is_active')



class ProfileDetailSerializer(serializers.ModelSerializer):
    """
    serializer for user that serialize :
    __all__
    based on default 'User' model
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'image', 'is_active')
