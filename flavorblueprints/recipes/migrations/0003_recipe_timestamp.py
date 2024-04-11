# Generated by Django 5.0.4 on 2024-04-11 17:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "recipes",
            "0002_primarycategory_remove_recipe_categories_subcategory_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="timestamp",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]