# Generated by Django 4.1.2 on 2023-01-27 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='age',
            field=models.CharField(choices=[('10M-18M', '10M-18M'), ('18M-36M', '18M-36M'), ('10M-36M', '10M-36M')], max_length=10),
        ),
    ]
