from .models import Recipe, Photo

def get_recipes_with_photos(recipes):
    """
    Takes a list of Recipes, and returns a list of tuples associating
    them to their first related Photo.

    The returned tuples have the form (Recipe, Photo).
    """
    recipes_with_photos: list[tuple[Recipe, Photo]] = []
    for recipe in recipes:
        photo = Photo.objects.filter(recipe=recipe)[0]
        recipes_with_photos.append((recipe, photo))
    return recipes_with_photos
