# Generated by Django 4.1.1 on 2023-08-27 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0092_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='quantity',
            field=models.SmallIntegerField(default=1, verbose_name='Quantity'),
        ),
    ]
