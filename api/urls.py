from rest_framework import routers

from api.views import UserViewSet, PhotoViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"photos", PhotoViewSet, basename="photo")
urlpatterns = router.urls
