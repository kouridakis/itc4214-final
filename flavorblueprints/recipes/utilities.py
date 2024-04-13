from typing import TypedDict
from django.db.models import QuerySet
from .models import Recipe, Photo, Star


class RecipeBundle(TypedDict):
    recipe: Recipe
    photo: Photo
    stars: int

def get_recipe_bundles(recipes: QuerySet[Recipe]) -> list[RecipeBundle]:
    """
    Takes a list of Recipes, and returns a list of RecipeBundles
    associating each Recipe with its first Photo and the number of Stars it has.
    """
    bundles: list[RecipeBundle] = []
    for recipe in recipes:
        photo = Photo.objects.filter(recipe=recipe)[0]
        stars = Star.objects.filter(recipe=recipe)
        bundles.append({
            "recipe": recipe,
            "photo": photo,
            "stars": len(stars)
        })
    return bundles
