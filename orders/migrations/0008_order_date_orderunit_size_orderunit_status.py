# Generated by Django 4.1.7 on 2023-08-02 16:30

import datetime
from django.db import migrations, models
import django.db.models.deletion
import orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_sizetranslationrows'),
        ('orders', '0007_order_bonus_sale_order_promo_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 2, 16, 30, 35, 467407, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='orderunit',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_units', to='products.sizetranslationrows'),
        ),
        migrations.AddField(
            model_name='orderunit',
            name='status',
            field=models.ForeignKey(default=orders.models.get_default_status, on_delete=django.db.models.deletion.PROTECT, related_name='order_units', to='orders.status'),
        ),
    ]
