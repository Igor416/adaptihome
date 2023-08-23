# Generated by Django 4.0.5 on 2022-07-05 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_basis_options_alter_bed_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedsheets',
            name='bedsheets_color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bedsheets_color', to='api.choice', verbose_name='Цвет комплекта'),
        ),
        migrations.AlterField(
            model_name='bedsheets',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packageBS', to='api.choice', verbose_name='Упаковка'),
        ),
        migrations.AlterField(
            model_name='bedsheets',
            name='tissue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tissue', to='api.choice', verbose_name='Ткань'),
        ),
        migrations.AlterField(
            model_name='blanket',
            name='blanket_color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blanket_color', to='api.choice', verbose_name='Цвет одеяла'),
        ),
        migrations.AlterField(
            model_name='blanket',
            name='filling',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filling', to='api.choice', verbose_name='Наполнитель'),
        ),
        migrations.AlterField(
            model_name='blanket',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packageBl', to='api.choice', verbose_name='Упаковка'),
        ),
        migrations.AlterField(
            model_name='mattrass',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection', to='api.choice', verbose_name='Коллекция'),
        ),
        migrations.AlterField(
            model_name='mattrass',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packageM', to='api.choice', verbose_name='Упаковка'),
        ),
        migrations.AlterField(
            model_name='mattrass',
            name='rigidity1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rigidity1', to='api.choice', verbose_name='Уровень жесткости стороны 1'),
        ),
        migrations.AlterField(
            model_name='mattrass',
            name='rigidity2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rigidity2', to='api.choice', verbose_name='Уровень жесткости стороны 2'),
        ),
        migrations.AlterField(
            model_name='mattrass',
            name='springblock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='springblock', to='api.choice', verbose_name='Пружинный блок'),
        ),
        migrations.AlterField(
            model_name='mattrasspad',
            name='binding',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='binding', to='api.choice', verbose_name='Крепление'),
        ),
        migrations.AlterField(
            model_name='pillow',
            name='material_filler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_filler', to='api.choice', verbose_name='Материал наполнения'),
        ),
        migrations.AlterField(
            model_name='stand',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material', to='api.choice', verbose_name='Материал'),
        ),
    ]
