# Generated by Django 4.1.2 on 2023-01-30 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0004_alter_menu_price'),
        ('accounts', '0007_alter_child_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='orders',
            field=models.ManyToManyField(blank=True, to='menu_app.menu'),
        ),
    ]
