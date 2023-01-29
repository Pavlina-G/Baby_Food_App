# Generated by Django 4.1.2 on 2023-01-29 13:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.FloatField(default=3.5, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]