# Generated by Django 4.1.7 on 2023-08-19 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_headertext_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headertext',
            name='text',
            field=models.CharField(default='', max_length=8096),
        ),
    ]
