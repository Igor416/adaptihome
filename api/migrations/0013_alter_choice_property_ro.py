# Generated by Django 4.0.5 on 2022-07-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_basis_legs_height_alter_mattrass_height_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='property_ro',
            field=models.CharField(max_length=32, verbose_name='Вариант выбора (ro)'),
        ),
    ]
