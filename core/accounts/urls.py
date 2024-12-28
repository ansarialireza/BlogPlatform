from django.urls import path
from .views import LoginView, LogoutView, RegisterView, UserCreate

app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path('users/',UserCreate.as_view(),name='user_create')
]
