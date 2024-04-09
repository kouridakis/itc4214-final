from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    supercategory = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients_metric = models.TextField()
    ingredients_imperial = models.TextField()
    instructions = models.TextField()
    categories = models.ManyToManyField(Category)
    def __str__(self):
        return self.title


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    alt_text = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
