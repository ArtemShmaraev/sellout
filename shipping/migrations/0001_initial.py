# Generated by Django 4.1.7 on 2023-06-24 13:43

from django.db import migrations, models
import django.db.models.deletion
import shipping.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('post_index', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=255)),
                ('site', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_price', models.IntegerField()),
                ('final_price', models.IntegerField()),
                ('url', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('availability', models.BooleanField(default=True)),
                ('warehouse', models.BooleanField(default=False)),
                ('is_multiple', models.BooleanField(default=False)),
                ('is_return', models.BooleanField(default=False)),
                ('is_fast_shipping', models.BooleanField(default=False)),
                ('is_sale', models.BooleanField(default=False)),
                ('currency', models.ForeignKey(default=shipping.models.get_default_currency, on_delete=django.db.models.deletion.CASCADE, to='utils.currency')),
                ('delivery_type', models.ForeignKey(default=shipping.models.get_default_delivery_type, on_delete=django.db.models.deletion.CASCADE, related_name='product_units', to='shipping.deliverytype')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_units', to='shipping.platform')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_units', to='products.product')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_units', to='products.sizetranslationrows')),
            ],
        ),
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moscow_del_price', models.IntegerField()),
                ('extra_charge_percentage', models.FloatField()),
                ('rounding_step', models.IntegerField(default=500)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='formulas', to='products.brand')),
                ('delivery_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='formulas', to='shipping.deliverytype')),
            ],
        ),
    ]