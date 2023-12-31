# Generated by Django 4.1.1 on 2022-10-20 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0075_auto_20221001_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='discount',
            field=models.SmallIntegerField(default=0, verbose_name='Скидка (%)'),
        ),
        migrations.AlterField(
            model_name='bedsheets',
            name='sizes',
            field=models.ManyToManyField(related_name='sizes%(class)s', to='api.bedsheetssize', verbose_name='Размеры'),
        ),
        migrations.AlterField(
            model_name='bedsheetssize',
            name='duvet_cover_size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='duvet_cover_size%(class)s', to='api.size', verbose_name='Пододеяльник'),
        ),
        migrations.AlterField(
            model_name='bedsheetssize',
            name='elasticated_sheet_size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='elasticated_sheet_size%(class)s', to='api.size', verbose_name='Простыня на резинке'),
        ),
        migrations.AlterField(
            model_name='bedsheetssize',
            name='pillowcase_sizes',
            field=models.ManyToManyField(related_name='pillowcase_sizes%(class)s', to='api.size', verbose_name='Наволочки'),
        ),
        migrations.AlterField(
            model_name='bedsheetssize',
            name='sheet_size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sheet_size%(class)s', to='api.size', verbose_name='Простыня'),
        ),
        migrations.AlterField(
            model_name='blanket',
            name='age',
            field=models.ManyToManyField(related_name='age%(class)s', to='api.choice'),
        ),
        migrations.AlterField(
            model_name='blanket',
            name='cover',
            field=models.ManyToManyField(related_name='cover%(class)s', to='api.choice'),
        ),
        migrations.AlterField(
            model_name='blanket',
            name='filling',
            field=models.ManyToManyField(related_name='filling%(class)s', to='api.choice'),
        ),
        migrations.AlterField(
            model_name='marker',
            name='name',
            field=models.CharField(max_length=64, primary_key=True, serialize=False, unique=True, verbose_name='Маркер'),
        ),
        migrations.AlterField(
            model_name='mattress',
            name='age',
            field=models.ManyToManyField(related_name='age%(class)s', to='api.choice'),
        ),
        migrations.AlterField(
            model_name='mattress',
            name='rigidity1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rigidity1%(class)s', to='api.choice'),
        ),
        migrations.AlterField(
            model_name='mattress',
            name='rigidity2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rigidity2%(class)s', to='api.choice'),
        ),
        migrations.AlterField(
            model_name='mattress',
            name='structure',
            field=models.ManyToManyField(blank=True, related_name='structure_%(class)s', through='api.LayerMattress', to='api.technology', verbose_name='Структура'),
        ),
        migrations.AlterField(
            model_name='mattress',
            name='technologies',
            field=models.ManyToManyField(blank=True, related_name='technologies_%(class)s', to='api.technology', verbose_name='Технологии'),
        ),
        migrations.AlterField(
            model_name='mattresspad',
            name='age',
            field=models.ManyToManyField(related_name='age%(class)s', to='api.choice'),
        ),
        migrations.AlterField(
            model_name='mattresspad',
            name='cover',
            field=models.ManyToManyField(related_name='cover%(class)s', to='api.choice'),
        ),
        migrations.AlterField(
            model_name='mattresspad',
            name='structure',
            field=models.ManyToManyField(blank=True, related_name='structure_%(class)s', through='api.LayerMattressPad', to='api.technology', verbose_name='Структура'),
        ),
        migrations.AlterField(
            model_name='mattresspad',
            name='technologies',
            field=models.ManyToManyField(blank=True, related_name='technologies_%(class)s', to='api.technology', verbose_name='Технологии'),
        ),
        migrations.AlterField(
            model_name='pillow',
            name='age',
            field=models.ManyToManyField(related_name='age%(class)s', to='api.choice'),
        ),
        migrations.AlterField(
            model_name='pillow',
            name='cover',
            field=models.ManyToManyField(related_name='cover%(class)s', to='api.choice'),
        ),
        migrations.AlterField(
            model_name='pillow',
            name='structure',
            field=models.ManyToManyField(blank=True, related_name='structure_%(class)s', through='api.LayerPillow', to='api.technology', verbose_name='Структура'),
        ),
    ]
