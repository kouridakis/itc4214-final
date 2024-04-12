from django.urls import path
from . import views

app_name = "recipes"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:primary_category_name>/<str:subcategory_name>/", views.category, name="category"),
    path("<str:primary_category_name>/<str:subcategory_name>/<str:recipe_title>/", views.recipe, name="recipe"),
]
