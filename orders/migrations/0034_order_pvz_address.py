# Generated by Django 4.1.7 on 2023-09-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0033_alter_order_status_alter_orderunit_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pvz_address',
            field=models.CharField(default='', max_length=2048),
        ),
    ]
