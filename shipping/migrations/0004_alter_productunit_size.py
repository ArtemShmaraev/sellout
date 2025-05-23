# Generated by Django 4.1.7 on 2023-08-01 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_sizetranslationrows'),
        ('shipping', '0003_addressinfo_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productunit',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_units', to='products.sizetranslationrows'),
        ),
    ]
