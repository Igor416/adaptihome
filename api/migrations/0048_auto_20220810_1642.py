# Generated by Django 3.1.3 on 2022-08-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0047_auto_20220806_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='Фотография'),
        ),
    ]
