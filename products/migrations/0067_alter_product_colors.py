# Generated by Django 4.1.7 on 2023-10-19 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0066_remove_dewuinfo_processed_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(blank=True, related_name='products', to='products.color'),
        ),
    ]
