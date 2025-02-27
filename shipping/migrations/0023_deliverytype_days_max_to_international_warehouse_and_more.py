# Generated by Django 4.1.7 on 2023-09-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0022_alter_productunit_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverytype',
            name='days_max_to_international_warehouse',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deliverytype',
            name='days_max_to_russian_warehouse',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deliverytype',
            name='days_min_to_international_warehouse',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deliverytype',
            name='days_min_to_russian_warehouse',
            field=models.IntegerField(default=0),
        ),
    ]
