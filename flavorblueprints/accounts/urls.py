from django.urls import path, include
from django.contrib.auth.views import LoginView, PasswordChangeView
from . import views

app_name = "accounts"

urlpatterns = [
    # Defines views for login, logout, password_change, and password_reset.
    path(f"{app_name}/login/", LoginView.as_view(), name="login"),
    path(f"{app_name}/logout/", views.logout, name="logout"),
    path(f"{app_name}/password_change/", PasswordChangeView.as_view(), name="password_change"),
    path(f"{app_name}/register/", views.register, name="register"),
    path(f"{app_name}/profile/", views.profile, name="profile")
]
