# Generated by Django 3.1.3 on 2022-08-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_auto_20220804_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='bed',
            name='lifetime',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='blanket',
            name='cover',
            field=models.ManyToManyField(related_name='coverblanket', to='api.Choice'),
        ),
    ]
