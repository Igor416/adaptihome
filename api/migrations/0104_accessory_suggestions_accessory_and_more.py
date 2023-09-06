# Generated by Django 4.1.1 on 2023-09-05 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0103_remove_accessory_suggestions_accessory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessory',
            name='suggestions_Accessory',
            field=models.ManyToManyField(to='api.accessory'),
        ),
        migrations.AddField(
            model_name='basis',
            name='suggestions_Bed',
            field=models.ManyToManyField(to='api.bed'),
        ),
        migrations.AddField(
            model_name='basis',
            name='suggestions_Mattress',
            field=models.ManyToManyField(to='api.mattress'),
        ),
        migrations.AddField(
            model_name='bed',
            name='suggestions_Mattress',
            field=models.ManyToManyField(to='api.mattress'),
        ),
        migrations.AddField(
            model_name='bed',
            name='suggestions_Puff',
            field=models.ManyToManyField(to='api.puff'),
        ),
        migrations.AddField(
            model_name='blanket',
            name='suggestions_MattressPad',
            field=models.ManyToManyField(to='api.mattresspad'),
        ),
        migrations.AddField(
            model_name='blanket',
            name='suggestions_Pillow',
            field=models.ManyToManyField(to='api.pillow'),
        ),
        migrations.AddField(
            model_name='foldingbed',
            name='suggestions_Mattress',
            field=models.ManyToManyField(to='api.mattress'),
        ),
        migrations.AddField(
            model_name='foldingbed',
            name='suggestions_Puff',
            field=models.ManyToManyField(to='api.puff'),
        ),
        migrations.AddField(
            model_name='mattress',
            name='suggestions_MattressPad',
            field=models.ManyToManyField(to='api.mattresspad'),
        ),
        migrations.AddField(
            model_name='mattress',
            name='suggestions_Pillow',
            field=models.ManyToManyField(to='api.pillow'),
        ),
        migrations.AddField(
            model_name='mattresspad',
            name='suggestions_Blanket',
            field=models.ManyToManyField(to='api.blanket'),
        ),
        migrations.AddField(
            model_name='mattresspad',
            name='suggestions_Pillow',
            field=models.ManyToManyField(to='api.pillow'),
        ),
        migrations.AddField(
            model_name='pillow',
            name='suggestions_Blanket',
            field=models.ManyToManyField(to='api.blanket'),
        ),
        migrations.AddField(
            model_name='pillow',
            name='suggestions_MattressPad',
            field=models.ManyToManyField(to='api.mattresspad'),
        ),
        migrations.AddField(
            model_name='puff',
            name='suggestions_FoldingBed',
            field=models.ManyToManyField(to='api.foldingbed'),
        ),
        migrations.AddField(
            model_name='table',
            name='suggestions_Accessory',
            field=models.ManyToManyField(to='api.accessory'),
        ),
    ]
