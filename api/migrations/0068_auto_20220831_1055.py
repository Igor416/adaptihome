# Generated by Django 3.1.3 on 2022-08-31 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0067_auto_20220831_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedsheets',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Название'),
        ),
    ]
