from django.shortcuts import render
from django.http import Http404
from .models import PrimaryCategory, SubCategory, Recipe, Photo, Star
from .utilities import get_recipe_bundles

# Create your views here.
def index(request):
    # Get 10 most recent recipes
    # Not very useful in this case, as there are only 5 total recipes,
    # but good for future reference.
    recipes = Recipe.objects.order_by("-timestamp")
    if len(recipes) > 10:
        recipes = recipes[:10]

    bundles = get_recipe_bundles(recipes)

    return render(request, "recipes/index.html", {
        "user": request.user if request.user.is_authenticated else None,
        "bundles": bundles
    })

def recipe(request, primary_category_name, subcategory_name, recipe_title):
    primary_category_name = primary_category_name.replace("-", " ")
    subcategory_name = subcategory_name.replace("-", " ")
    recipe_title = recipe_title.replace("-", " ")

    try:
        # Cannot use __iexact with ForeignKey
        primary_category = PrimaryCategory.objects.get(name__iexact=primary_category_name)
        subcategory = SubCategory.objects.get(
            name__iexact=subcategory_name, 
            primary_category=primary_category)
        recipe = Recipe.objects.get(
            title__iexact=recipe_title, 
            category=subcategory)
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
    recommendations = Recipe.objects.filter(category=recipe.category).exclude(pk=recipe.id)
    # Fall back to the same primary category if there are not enough recommendations
    if len(recommendations) < 3:
        primary_category = recipe.category.primary_category
        other_categories = SubCategory.objects.filter(primary_category=primary_category)
        recommendations = Recipe.objects.filter(category__in=other_categories).exclude(pk=recipe.id)
    
    bundles = get_recipe_bundles(recommendations)

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
        "recommendations": bundles
    })

def category(request, primary_category_name, subcategory_name):
    primary_category_name = primary_category_name.replace("-", " ")
    subcategory_name = subcategory_name.replace("-", " ")

    try:
        # Cannot use __iexact with ForeignKey
        primary_category = PrimaryCategory.objects.get(name__iexact=primary_category_name)
        # Case insensitive search
        category = SubCategory.objects.get(
            name__iexact=subcategory_name, 
            primary_category=primary_category)
    except Recipe.DoesNotExist:
        raise Http404("Category does not exist")
    
    recipes = Recipe.objects.filter(category=category)
    bundles = get_recipe_bundles(recipes)

    return render(request, "recipes/category.html", {
        "category": category,
        "bundles": bundles
    })
