# Generated by Django 3.1.3 on 2022-07-29 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_auto_20220729_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Фото товара'),
        ),
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Фото товара'),
        ),
    ]
