from django_filters import rest_framework as filters
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.serializers import PhotoSerializer, UserSerializer
from photo.models import Photo

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['location', 'date', "people"]

    def get_queryset(self):
        user = self.request.user
        if user:
            return Photo.objects.filter(user__pk=user.pk)

