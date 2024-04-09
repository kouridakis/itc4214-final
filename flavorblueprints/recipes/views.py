from django.shortcuts import render
from django.http import Http404
from .models import Recipe, Photo

# Create your views here.
def index(request):
    return render(request, "recipes/index.html")

def recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    
    photos = Photo.objects.filter(recipe=recipe)
    return render(request, "recipes/recipe.html", {
        "recipe": recipe,
        "photos": photos
    })
