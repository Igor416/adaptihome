# Generated by Django 3.1.3 on 2022-07-29 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_auto_20220728_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video',
        ),
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(default='', upload_to='videos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='video_id',
            field=models.CharField(default='', max_length=64, unique=True, verbose_name='Ссылка на видео'),
            preserve_default=False,
        ),
    ]
