# Generated by Django 4.1.2 on 2023-01-23 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.CharField(default='Burgas', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(default='Burgas', max_length=20),
        ),
    ]
