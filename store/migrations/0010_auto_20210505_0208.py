# Generated by Django 3.2 on 2021-05-04 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_product_fuel_capacity_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='fuel_capacity',
            field=models.FloatField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='fuel_capacity_unit',
            field=models.CharField(blank=True, choices=[('select', 'SELECT'), ('liters', 'LITERS'), ('cc', 'CC')], default='liters', max_length=10, null=True),
        ),
    ]