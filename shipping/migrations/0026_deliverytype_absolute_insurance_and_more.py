# Generated by Django 4.1.7 on 2023-09-08 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0025_productunit_extra_delivery_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverytype',
            name='absolute_insurance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deliverytype',
            name='decimal_insurance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deliverytype',
            name='delivery_price_per_kg_in_rub',
            field=models.IntegerField(default=0),
        ),
    ]
