from django.urls import path
from . import views

app_name = "search"
urlpatterns = [
    path(f"{app_name}/", views.index, name="index"),
    path(f"{app_name}/<str:query>/", views.search, name="search")
]
