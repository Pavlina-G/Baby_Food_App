# Generated by Django 4.1.2 on 2022-12-22 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_allergens_alter_recipe_weight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipewithoutallergens',
            name='allergens',
            field=models.CharField(blank=True, default='NO', editable=False, max_length=2),
        ),
    ]