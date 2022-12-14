from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from knox import views as knox_views
from rest_framework import permissions, routers

from api.views import LoginAPI, PhotoViewSet, RegisterAPI, UserViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Photo Manager API",
        default_version="v1",
        description="Save your photos here",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="koval6polina@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"photos", PhotoViewSet, basename="photo")
urlpatterns = router.urls

urlpatterns += [
    path("register/", RegisterAPI.as_view(), name="register"),
    path("login/", LoginAPI.as_view(), name="login"),
    path("logout/", knox_views.LogoutView.as_view(), name="logout"),
    path("logoutall/", knox_views.LogoutAllView.as_view(), name="logoutall"),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
