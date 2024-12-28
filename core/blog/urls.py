from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet,CategoryViewSet

router = DefaultRouter()
router.register(r'posts',PostViewSet)
router.register(r'categories',CategoryViewSet)

urlpatterns = router.urls
