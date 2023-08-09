# Generated by Django 4.1.2 on 2023-07-29 18:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_payments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='card_expiry_year',
            field=models.IntegerField(choices=[(2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027)], validators=[django.core.validators.MinValueValidator(2023), django.core.validators.MaxValueValidator(2028)]),
        ),
    ]