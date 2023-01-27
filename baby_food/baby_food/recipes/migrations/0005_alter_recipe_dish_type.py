# Generated by Django 4.1.2 on 2023-01-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_remove_recipe_allergens_alter_recipe_dish_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='dish_type',
            field=models.CharField(choices=[('SOUP', 'SOUP'), ('MAIN DISH', 'MAIN DISH'), ('DESSERT', 'DESSERT'), ('ALLERGY FREE SOUP', 'AF SOUP'), ('AF MAIN DISH', 'AF MAIN DISH'), ('AF DESSERT', 'AF DESSERT')], max_length=20),
        ),
    ]
