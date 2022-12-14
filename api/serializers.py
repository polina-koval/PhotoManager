from django.contrib.auth import get_user_model
from rest_framework import serializers

from photo.models import Photo

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


class PhotoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ["id", "image"]


class PhotoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ["id", "location", "date", "description", "people", "image"]

    def create(self, validated_data):
        user = self.context["request"].user
        photo = Photo.objects.create(user=user, ** validated_data)
        return photo
