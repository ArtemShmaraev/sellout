# Generated by Django 4.1.7 on 2023-10-15 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0060_brand_search_filter_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='search_filter_name',
        ),
        migrations.AddField(
            model_name='line',
            name='search_filter_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
