# Generated by Django 4.1.2 on 2023-01-23 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='number_of_children',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
