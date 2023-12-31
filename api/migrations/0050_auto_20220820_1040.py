# Generated by Django 3.1.3 on 2022-08-20 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0049_auto_20220812_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=64, verbose_name='Маркер (en)')),
                ('name_ru', models.CharField(max_length=64, verbose_name='Маркер (ru)')),
                ('name_ro', models.CharField(max_length=64, verbose_name='Маркер (ro)')),
            ],
            options={
                'verbose_name': 'маркер',
                'verbose_name_plural': 'маркеры',
            },
        ),
        migrations.AddField(
            model_name='mattress',
            name='markers',
            field=models.ManyToManyField(related_name='markers', to='api.Marker', verbose_name='Маркеры'),
        ),
    ]
