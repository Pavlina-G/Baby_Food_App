# Generated by Django 4.1.2 on 2023-07-22 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_alter_category_options'),
        ('accounts', '0013_alter_child_first_name_alter_child_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.location'),
        ),
    ]