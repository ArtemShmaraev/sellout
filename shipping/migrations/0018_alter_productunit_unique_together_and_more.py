# Generated by Django 4.1.7 on 2023-09-05 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0040_product_products_pr_id_b46934_idx_and_more'),
        ('shipping', '0017_productunit_weight'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productunit',
            unique_together={('product', 'id')},
        ),
        migrations.AddIndex(
            model_name='productunit',
            index=models.Index(fields=['product', 'id'], name='shipping_pr_product_98e056_idx'),
        ),
    ]
