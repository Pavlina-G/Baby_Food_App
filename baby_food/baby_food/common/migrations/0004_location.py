# Generated by Django 4.1.2 on 2023-01-23 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_gallery_upload_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
