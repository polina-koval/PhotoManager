from django.contrib.auth import get_user_model, login
from django_filters.rest_framework import DjangoFilterBackend
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework import status, viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from api.serializers import (
    PhotoDetailSerializer,
    PhotoListSerializer,
    UserSerializer, RegisterSerializer,
)
from photo.filters import PhotoFilter
from photo.models import Photo

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterAPI(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (AllowAny, )

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


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
