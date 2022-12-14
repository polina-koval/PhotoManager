from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import (
    PhotoDetailSerializer,
    PhotoListSerializer,
    UserSerializer,
)
from photo.filters import PhotoFilter
from photo.models import Photo

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PhotoSerializer:
    pass


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoListSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PhotoFilter

    def get_queryset(self):
        user = self.request.user
        if user:
            return Photo.objects.filter(user__pk=user.pk)

    def get_serializer_class(self):
        if self.action in ("retrieve", "create"):
            return PhotoDetailSerializer
        return PhotoListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
