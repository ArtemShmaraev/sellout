# Generated by Django 4.1.7 on 2023-09-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.CharField(default='', max_length=4048),
        ),
    ]
