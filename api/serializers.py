from django.contrib.auth import get_user_model
from rest_framework import serializers

from photo.models import Photo

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ["id", "location", "description", "user", "image", "people"]
