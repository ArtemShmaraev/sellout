# Generated by Django 4.1.7 on 2023-08-03 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_date_orderunit_size_orderunit_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 3, 12, 52, 53, 229028, tzinfo=datetime.timezone.utc)),
        ),
    ]
