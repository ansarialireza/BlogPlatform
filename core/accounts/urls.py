from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LoginView, LogoutView, RegisterView, UserViewSet

app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]

router = DefaultRouter()
router.register(r'users',UserViewSet)
urlpatterns += router.urls

