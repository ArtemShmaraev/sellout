# Generated by Django 4.1.7 on 2023-08-07 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_sizerow_remove_sizetable_size_rows_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sizetable',
            name='default_row',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='default_size_table', to='products.sizerow'),
        ),
    ]
