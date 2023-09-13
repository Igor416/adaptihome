# Generated by Django 4.1.1 on 2023-09-13 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0109_alter_accessory_options_alter_basis_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='depth',
        ),
        migrations.AddField(
            model_name='table',
            name='dimensions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dimensions', to='api.size', verbose_name='Dimensions'),
        ),
        migrations.AddField(
            model_name='table',
            name='fixation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fixation', to='api.choice'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='name',
            field=models.CharField(choices=[('COMMON', 'COMMON'), ('age', 'Age Category'), ('rigidity', 'Rigidity level of side'), ('cover', 'Cover'), ('', ''), ('FoldingBed', 'ONLY MURHY BED'), ('base', 'Mattress Base'), ('wall', 'Recommended wall for fastening'), ('legs', 'Legs'), ('cushion', 'Back cushion'), ('', ''), ('Bed', 'ONLY BED'), ('bed_type', 'Bed Type'), ('', ''), ('Mattress', 'ONLY MATTRESS'), ('mattress_type', 'Mattress Type'), ('collection', 'Collection'), ('construction', 'Construction'), ('rigidity', 'Rigidity level of side'), ('springblock', 'Spring block'), ('', ''), ('Table', 'ONLY TABLE'), ('swivel_leg', 'Swivel leg'), ('fixation', 'Fixation system'), ('', ''), ('Pillow', 'ONLY PILLOW'), ('material_filler', 'Material Filler'), ('', ''), ('MattressPad', 'ONLY MATTRESS PAD'), ('mattresspad_type', 'Mattress Pad Type'), ('rigidity', 'Rigidity level of side'), ('binding', 'Contour'), ('', ''), ('Blanket', 'ONLY BLANKET'), ('blanket_type', 'Blanket Type'), ('blanket_color', 'Blanket Color'), ('filling', 'Filling'), ('', ''), ('Puff', 'ONLY PUFF'), ('material', 'Material'), ('', ''), ('Accessory', 'ONLY ACCESSORY')], max_length=32, verbose_name='Characteristic'),
        ),
    ]
