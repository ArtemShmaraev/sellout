# Generated by Django 4.1.7 on 2023-06-26 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0002_deliverytype_view_name'),
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOrderUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_price', models.IntegerField(blank=True, null=True)),
                ('final_price', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(default='', max_length=127)),
                ('product_unit', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='shipping.productunit')),
            ],
        ),
    ]