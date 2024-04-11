from django.shortcuts import render
from django.http import Http404
from .models import SubCategory, Recipe, Photo
from .utilities import get_recipes_with_photos

# Create your views here.
def index(request):
    # Get 10 most recent recipes
    # Not very useful in this case, as there are only 5 total recipes,
    # but good for future reference.
    recipes = Recipe.objects.order_by("-timestamp")
    if len(recipes) > 10:
        recipes = recipes[:10]

    recipes_with_photos = get_recipes_with_photos(recipes)

    return render(request, "recipes/index.html", {
        "recipes_with_photos": recipes_with_photos
    })

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

def category(request, category_id):
    try:
        category = SubCategory.objects.get(pk=category_id)
    except Recipe.DoesNotExist:
        raise Http404("Category does not exist")
    
    recipes = Recipe.objects.filter(category=category)
    recipes_with_photos = get_recipes_with_photos(recipes)

    return render(request, "recipes/category.html", {
        "category": category,
        "recipes_with_photos": recipes_with_photos
    })
