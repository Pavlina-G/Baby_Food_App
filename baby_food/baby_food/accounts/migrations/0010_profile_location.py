# Generated by Django 4.1.2 on 2023-02-09 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_alter_category_options'),
        ('accounts', '0009_remove_profile_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='common.location'),
            preserve_default=False,
        ),
    ]