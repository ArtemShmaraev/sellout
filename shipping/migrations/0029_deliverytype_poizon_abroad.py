# Generated by Django 4.1.7 on 2023-09-08 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0028_productunit_approximate_price_with_delivery_in_rub'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverytype',
            name='poizon_abroad',
            field=models.BooleanField(default=False),
        ),
    ]
