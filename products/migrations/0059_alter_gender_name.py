# Generated by Django 4.1.7 on 2023-10-13 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0058_product_products_pr_id_b46934_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='name',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('K', 'Kids')], db_index=True, max_length=255),
        ),
    ]
