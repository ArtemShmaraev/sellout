# Generated by Django 4.1.7 on 2023-09-05 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0037_alter_product_rel_num'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['id'], name='products_pr_id_b46934_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['spu_id'], name='products_pr_spu_id_f4ec58_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['model'], name='products_pr_model_268e30_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['colorway'], name='products_pr_colorwa_e9728c_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['slug'], name='products_pr_slug_3edc0c_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['manufacturer_sku'], name='products_pr_manufac_be8e97_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['is_custom'], name='products_pr_is_cust_9419ae_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['is_collab'], name='products_pr_is_coll_001e82_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['min_price'], name='products_pr_min_pri_3029f2_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['rel_num'], name='products_pr_rel_num_530f30_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['available_flag'], name='products_pr_availab_aa08f7_idx'),
        ),
    ]
