# Generated by Django 4.1.7 on 2023-10-17 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0061_remove_brand_search_filter_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerphoto',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
