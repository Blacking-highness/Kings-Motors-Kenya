# Generated by Django 3.2 on 2021-05-04 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20210505_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='details',
            field=models.TextField(default=True, max_length=2000),
        ),
    ]
