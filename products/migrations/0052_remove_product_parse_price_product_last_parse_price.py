# Generated by Django 4.1.7 on 2023-09-22 15:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0051_product_parse_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='parse_price',
        ),
        migrations.AddField(
            model_name='product',
            name='last_parse_price',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
