# Generated by Django 4.1.2 on 2023-08-06 11:58

import baby_food.common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_child_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='date_of_birth',
            field=models.DateField(null=True, validators=[baby_food.common.validators.validate_birth_date]),
        ),
    ]
