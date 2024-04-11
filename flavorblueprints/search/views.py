from string import punctuation
from django.shortcuts import render
from django.db.models import Q, QuerySet
from recipes.models import Recipe
from recipes.utilities import get_recipes_with_photos

def per_word_search(query: str) -> QuerySet:
    """
    Filters recipes based on each word in the query, 
    instead of the whole query as a single string.
    """
    query = query.strip().replace(",", "").replace(".", "")
    words = query.split(" ")

    filter = Q()
    for word in words:
        # Logical OR is used for the temp_filter, as the word showing up in any of
        # the specified fields is valid.
        temp_filter = Q()
        temp_filter |= Q(title__icontains=word)
        temp_filter |= Q(description__icontains=word)
        temp_filter |= Q(ingredients_metric__icontains=word)
        temp_filter |= Q(ingredients_imperial__icontains=word)
        # Logical AND is used to connect it to the main filter,
        # as all words should be present in a recipe for it to qualify.
        filter &= temp_filter
    
    return Recipe.objects.filter(filter)

# Create your views here.
def index(request):
    return render(request, "search/search.html", {
        "query": "",
        "recipes_with_photos": None
    })

def search(request, query):
    recipes = per_word_search(query)

    recipes_with_photos = get_recipes_with_photos(recipes)

    return render(request, "search/search.html", {
        "query": query,
        "recipes_with_photos": recipes_with_photos
    })
