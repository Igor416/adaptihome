# Generated by Django 4.1.1 on 2023-09-12 19:13

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0108_foldingbed_article_en_foldingbed_article_gr_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accessory',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='basis',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='bed',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='blanket',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='foldingbed',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='mattress',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='mattresspad',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='pillow',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='puff',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'ordering': [django.db.models.expressions.CombinedExpression(models.F('price'), '*', django.db.models.expressions.CombinedExpression(models.Value(100), '-', django.db.models.expressions.CombinedExpression(models.F('discount'), '/', models.Value(100))))], 'verbose_name': 'size', 'verbose_name_plural': 'sizes'},
        ),
        migrations.AlterModelOptions(
            name='table',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='table',
            name='article_en',
            field=models.TextField(blank=True, verbose_name='Article (gr)'),
        ),
        migrations.AddField(
            model_name='table',
            name='article_gr',
            field=models.TextField(blank=True, verbose_name='Article (en)'),
        ),
        migrations.AddField(
            model_name='table',
            name='seats',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='table',
            name='swivel_leg',
            field=models.ManyToManyField(related_name='swivel_leg', to='api.choice'),
        ),
    ]