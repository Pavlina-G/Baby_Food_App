# Generated by Django 4.1.2 on 2023-01-31 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0005_menu_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(choices=[('Allergy-Free Menu', 'Allergy-Free Menu'), ('Menu With Allergens', 'Menu With Allergens')], max_length=30),
        ),
    ]
