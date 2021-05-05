# Generated by Django 3.2 on 2021-05-04 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_customer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fuel_capacity',
            field=models.FloatField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(default='auto', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='transmission',
            field=models.CharField(choices=[('manual', 'MANUAL'), ('auto', 'AUTOMATIC')], default='auto', max_length=7),
        ),
    ]