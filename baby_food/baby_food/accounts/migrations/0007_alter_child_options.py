# Generated by Django 4.1.2 on 2023-01-23 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_appuser_number_of_children'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='child',
            options={'verbose_name_plural': 'Children'},
        ),
    ]
