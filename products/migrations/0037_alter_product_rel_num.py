# Generated by Django 4.1.7 on 2023-09-04 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0036_alter_headerphoto_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rel_num',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
