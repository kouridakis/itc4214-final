from django.contrib import admin
from .models import PrimaryCategory, SubCategory, Recipe, Photo

# Register your models here.
admin.site.register(PrimaryCategory)
admin.site.register(SubCategory)
admin.site.register(Recipe)
admin.site.register(Photo)
