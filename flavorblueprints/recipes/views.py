from django.shortcuts import render
from django.http import Http404
from .models import SubCategory, Recipe, Photo, Star
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
        "user": request.user if request.user.is_authenticated else None,
        "recipes_with_photos": recipes_with_photos
    })

def recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    
    # Handle rating
    if request.method == "POST" and request.user.is_authenticated:
        # Toggle star
        if len(Star.objects.filter(user=request.user, recipe=recipe)) > 0:
            Star.objects.filter(user=request.user, recipe=recipe).delete()
        else:
            Star.objects.create(user=request.user, recipe=recipe)

    
    title = recipe.title
    description = recipe.description
    ingredients_metric = recipe.ingredients_metric.split("\n")
    ingredients_imperial = recipe.ingredients_imperial.split("\n")
    instructions = recipe.instructions.split("\n")
    
    photos = Photo.objects.filter(recipe=recipe)

    # Get stars
    star_count = len(Star.objects.filter(recipe=recipe))

    # Check if the user has starred the recipe
    user_starred = False
    user = None
    if request.user.is_authenticated:
        user = request.user
        user_starred = len(Star.objects.filter(user=user, recipe=recipe)) > 0

    # Get recommendations from the same category
    recommendations = Recipe.objects.filter(category=recipe.category).exclude(pk=recipe_id)
    # Fall back to the same primary category if there are not enough recommendations
    if len(recommendations) < 3:
        primary_category = recipe.category.primary_category
        other_categories = SubCategory.objects.filter(primary_category=primary_category)
        recommendations = Recipe.objects.filter(category__in=other_categories).exclude(pk=recipe_id)
    
    recommendations = get_recipes_with_photos(recommendations)

    return render(request, "recipes/recipe.html", {
        "title": title,
        "description": description,
        "photos": photos,
        "ingredients_metric": ingredients_metric,
        "ingredients_imperial": ingredients_imperial,
        "instructions": instructions,
        "star_count": star_count,
        "user": user,
        "user_starred": user_starred,
        "recommendations": recommendations
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
