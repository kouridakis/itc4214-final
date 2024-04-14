# Generated by Django 5.0.4 on 2024-04-13 01:42

import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0005_star"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="primarycategory",
            options={"verbose_name_plural": "Primary Categories"},
        ),
        migrations.AlterModelOptions(
            name="subcategory",
            options={"verbose_name_plural": "Subcategories"},
        ),
        migrations.AddConstraint(
            model_name="primarycategory",
            constraint=models.UniqueConstraint(
                django.db.models.functions.text.Lower("name"),
                name="unique_primary_category",
            ),
        ),
        migrations.AddConstraint(
            model_name="recipe",
            constraint=models.UniqueConstraint(
                django.db.models.functions.text.Lower("title"),
                models.F("category"),
                name="unique_recipe",
            ),
        ),
        migrations.AddConstraint(
            model_name="subcategory",
            constraint=models.UniqueConstraint(
                django.db.models.functions.text.Lower("name"),
                models.F("primary_category"),
                name="unique_subcategory",
            ),
        ),
    ]