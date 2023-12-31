# Generated by Django 4.1.1 on 2023-09-08 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0107_alter_choice_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='foldingbed',
            name='article_en',
            field=models.TextField(blank=True, verbose_name='Article (gr)'),
        ),
        migrations.AddField(
            model_name='foldingbed',
            name='article_gr',
            field=models.TextField(blank=True, verbose_name='Article (en)'),
        ),
        migrations.AlterField(
            model_name='foldingbed',
            name='table_dimensions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='table_dimensions', to='api.size', verbose_name='Table Dimensions'),
        ),
    ]
