# Generated by Django 4.1.2 on 2023-07-29 11:24

import baby_food.common.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import encrypted_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_order_payment_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('order_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='order.order')),
                ('payment_number', models.CharField(max_length=80, unique=True, validators=[django.core.validators.MinLengthValidator(12), django.core.validators.MaxLengthValidator(12)])),
                ('card_holder', models.CharField(max_length=50)),
                ('card_number', models.PositiveBigIntegerField(validators=[baby_food.common.validators.validate_card_number])),
                ('card_expiry_year', models.IntegerField(choices=[(2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029)], validators=[django.core.validators.MinValueValidator(2023), django.core.validators.MaxValueValidator(2028)])),
                ('card_expiry_month', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])),
                ('card_verification_code', encrypted_fields.fields.EncryptedPositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)])),
                ('payment_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Payments',
                'ordering': ['-payment_date'],
            },
        ),
    ]
