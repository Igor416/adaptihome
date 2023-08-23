# Generated by Django 3.1.3 on 2022-08-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_auto_20220804_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pillow',
            name='structure',
        ),
        migrations.AlterField(
            model_name='technology',
            name='desc_en',
            field=models.TextField(verbose_name='Описание (en)'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='desc_ro',
            field=models.TextField(verbose_name='Описание (ro)'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='desc_ru',
            field=models.TextField(verbose_name='Описание (ru)'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='image',
            field=models.ImageField(default='', upload_to='images', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='name_en',
            field=models.CharField(blank=True, max_length=32, verbose_name='Название (en)'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='name_ro',
            field=models.CharField(blank=True, max_length=32, verbose_name='Название (ro)'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='name_ru',
            field=models.CharField(max_length=32, verbose_name='Название (ru)'),
        ),
    ]
