# Generated by Django 4.1.7 on 2023-10-03 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0035_alter_productunit_size_table'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='productunit',
            name='shipping_pr_product_98e056_idx',
        ),
        migrations.AlterUniqueTogether(
            name='productunit',
            unique_together=set(),
        ),
    ]
