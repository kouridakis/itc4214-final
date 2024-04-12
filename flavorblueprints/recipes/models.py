from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class PrimaryCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    primary_category = models.ForeignKey(PrimaryCategory, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} ({self.primary_category.name})"

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients_metric = models.TextField()
    ingredients_imperial = models.TextField()
    instructions = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    alt_text = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    def __str__(self):
        return self.alt_text

class Star(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username} starred {self.recipe.title}"
