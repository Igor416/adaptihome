# Generated by Django 4.1.1 on 2023-08-12 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0086_remove_bedsheetssize_duvet_cover_size_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='size',
            old_name='priceEUR',
            new_name='price',
        ),
    ]
