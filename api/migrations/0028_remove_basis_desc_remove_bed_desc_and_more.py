# Generated by Django 4.0.5 on 2022-07-17 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_alter_choice_category_alter_size_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basis',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='bed',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='bedsheets',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='blanket',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='mattrass',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='mattrasspad',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='pillow',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='stand',
            name='desc',
        ),
        migrations.AddField(
            model_name='basis',
            name='desc_en',
            field=models.TextField(default='', verbose_name='Описание (en)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basis',
            name='desc_ro',
            field=models.TextField(default='', verbose_name='Описание (ro)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basis',
            name='desc_ru',
            field=models.TextField(default='', verbose_name='Описание (ru)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bed',
            name='desc_en',
            field=models.TextField(default='', verbose_name='Описание (en)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bed',
            name='desc_ro',
            field=models.TextField(default='', verbose_name='Описание (ro)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bed',
            name='desc_ru',
            field=models.TextField(default='', verbose_name='Описание (ru)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bedsheets',
            name='desc_en',
            field=models.TextField(default='', verbose_name='Описание (en)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bedsheets',
            name='desc_ro',
            field=models.TextField(default='', verbose_name='Описание (ro)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bedsheets',
            name='desc_ru',
            field=models.TextField(default='', verbose_name='Описание (ru)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blanket',
            name='desc_en',
            field=models.TextField(default='', verbose_name='Описание (en)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blanket',
            name='desc_ro',
            field=models.TextField(default='', verbose_name='Описание (ro)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blanket',
            name='desc_ru',
            field=models.TextField(default='', verbose_name='Описание (ru)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mattrass',
            name='desc_en',
            field=models.TextField(default='', verbose_name='Описание (en)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mattrass',
            name='desc_ro',
            field=models.TextField(default='', verbose_name='Описание (ro)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mattrass',
            name='desc_ru',
            field=models.TextField(default='', verbose_name='Описание (ru)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mattrasspad',
            name='desc_en',
            field=models.TextField(default='', verbose_name='Описание (en)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mattrasspad',
            name='desc_ro',
            field=models.TextField(default='', verbose_name='Описание (ro)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mattrasspad',
            name='desc_ru',
            field=models.TextField(default='', verbose_name='Описание (ru)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pillow',
            name='desc_en',
            field=models.TextField(default='', verbose_name='Описание (en)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pillow',
            name='desc_ro',
            field=models.TextField(default='', verbose_name='Описание (ro)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pillow',
            name='desc_ru',
            field=models.TextField(default='', verbose_name='Описание (ru)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stand',
            name='desc_en',
            field=models.TextField(default='', verbose_name='Описание (en)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stand',
            name='desc_ro',
            field=models.TextField(default='', verbose_name='Описание (ro)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stand',
            name='desc_ru',
            field=models.TextField(default='', verbose_name='Описание (ru)'),
            preserve_default=False,
        ),
    ]
