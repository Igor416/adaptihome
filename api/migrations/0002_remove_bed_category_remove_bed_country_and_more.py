# Generated by Django 4.0.5 on 2022-06-26 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Basis',
        ),
        migrations.DeleteModel(
            name='Bed',
        ),
        migrations.DeleteModel(
            name='BedSheets',
        ),
        migrations.DeleteModel(
            name='Blanket',
        ),
        migrations.DeleteModel(
            name='Mattrass',
        ),
        migrations.DeleteModel(
            name='MattressPads',
        ),
        migrations.DeleteModel(
            name='Pillow',
        ),
        migrations.DeleteModel(
            name='Stand',
        ),
    ]
