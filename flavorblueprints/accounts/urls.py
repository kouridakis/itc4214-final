from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    # Defines views for login, logout, password_change, and password_reset.
    path(f"{app_name}/", include("django.contrib.auth.urls")),

    path(f"{app_name}/register/", views.register, name="register"),
    path(f"{app_name}/profile/", views.profile, name="profile")
]
