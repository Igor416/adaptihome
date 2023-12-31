# Generated by Django 3.1.3 on 2022-08-04 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0044_auto_20220804_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='mattress',
            name='structure',
            field=models.ManyToManyField(blank=True, related_name='structure_mattress', through='api.LayerMattress', to='api.Technology', verbose_name='Структура'),
        ),
        migrations.AddField(
            model_name='mattresspad',
            name='structure',
            field=models.ManyToManyField(blank=True, related_name='structure_mattresspad', through='api.LayerMattressPad', to='api.Technology', verbose_name='Структура'),
        ),
    ]
