# Generated by Django 4.1.2 on 2023-01-31 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_recipe_dish_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='added_on',
            field=models.DateField(auto_now=True),
        ),
    ]
