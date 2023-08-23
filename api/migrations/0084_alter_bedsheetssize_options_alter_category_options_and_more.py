# Generated by Django 4.1.1 on 2023-08-12 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0083_rename_name_ro_pl_category_name_gr_pl_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bedsheetssize',
            options={'verbose_name': 'bedsheets size', 'verbose_name_plural': 'bedsheets sizes'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'choice', 'verbose_name_plural': 'choices'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'photo', 'verbose_name_plural': 'photos'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': 'size', 'verbose_name_plural': 'sizes'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': 'stock', 'verbose_name_plural': 'stock'},
        ),
        migrations.AlterModelOptions(
            name='technology',
            options={'verbose_name': 'technology', 'verbose_name_plural': 'technologies'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'video', 'verbose_name_plural': 'videos'},
        ),
        migrations.RemoveField(
            model_name='mattress',
            name='markers',
        ),
        migrations.RemoveField(
            model_name='mattress',
            name='visible_markers',
        ),
        migrations.RemoveField(
            model_name='technology',
            name='isTechnology',
        ),
        migrations.AddField(
            model_name='technology',
            name='is_technology',
            field=models.BooleanField(default=False, verbose_name='Is technology (or layer)?'),
        ),
        migrations.AlterField(
            model_name='basis',
            name='desc_en',
            field=models.TextField(verbose_name='Описание (gr)'),
        ),
        migrations.AlterField(
            model_name='bed',
            name='desc_en',
            field=models.TextField(verbose_name='Описание (gr)'),
        ),
        migrations.AlterField(
            model_name='bedsheets',
            name='desc_en',
            field=models.TextField(verbose_name='Описание (gr)'),
        ),
        migrations.AlterField(
            model_name='bedsheets',
            name='name_en',
            field=models.CharField(max_length=32, verbose_name='Название (gr)'),
        ),
        migrations.AlterField(
            model_name='bedsheetssize',
            name='duvet_cover_size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='duvet_cover_size%(class)s', to='api.size', verbose_name='Duvet Cover'),
        ),
        migrations.AlterField(
            model_name='bedsheetssize',
            name='elasticated_sheet_size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='elasticated_sheet_size%(class)s', to='api.size', verbose_name='Elasticated Sheet'),
        ),
        migrations.AlterField(
            model_name='bedsheetssize',
            name='pillowcase_sizes',
            field=models.ManyToManyField(related_name='pillowcase_sizes%(class)s', to='api.size', verbose_name='Pillow Case'),
        ),
        migrations.AlterField(
            model_name='bedsheetssize',
            name='sheet_size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sheet_size%(class)s', to='api.size', verbose_name='Sheet'),
        ),
        migrations.AlterField(
            model_name='blanket',
            name='desc_en',
            field=models.TextField(verbose_name='Описание (gr)'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Mattress', 'Mattress'), ('Pillow', 'Pillow'), ('MattressPad', 'Mattress Pad'), ('Blanket', 'Blanket'), ('BedSheets', 'Bed Sheets Kit'), ('Bed', 'Bed'), ('Stand', 'Stand'), ('Basis', 'Basis')], max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_en_pl',
            field=models.CharField(max_length=32, verbose_name='English plural'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_en_s',
            field=models.CharField(max_length=32, verbose_name='English singular'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_gr_pl',
            field=models.CharField(max_length=32, verbose_name='Greek plural'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_gr_s',
            field=models.CharField(max_length=32, verbose_name='Greek singular'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='category',
            field=models.ManyToManyField(to='api.category'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='name',
            field=models.CharField(choices=[('ОБЩИЕ', 'ОБЩИЕ'), ('age', 'Age Category'), ('rigidity', 'Rigidity level of side'), ('cover', 'Cover'), ('', ''), ('Mattress', 'ТОЛЬКО MATTRESS'), ('mattress_type', 'Mattress Type'), ('collection', 'Collection'), ('construction', 'Construction'), ('rigidity', 'Rigidity level of side'), ('springblock', 'Spring block'), ('', ''), ('Pillow', 'ТОЛЬКО PILLOW'), ('material_filler', 'Material Filler'), ('', ''), ('MattressPad', 'ТОЛЬКО MATTRESS PAD'), ('mattresspad_type', 'Mattress Pad Type'), ('rigidity', 'Rigidity level of side'), ('binding', 'Contour'), ('', ''), ('Blanket', 'ТОЛЬКО BLANKET'), ('blanket_type', 'Blanket Type'), ('blanket_color', 'Blanket Color'), ('filling', 'Filling'), ('', ''), ('BedSheets', 'ТОЛЬКО BED SHEETS KIT'), ('bedsheets_type', 'Kit Type'), ('bedsheets_color', 'Kit color'), ('tissue', 'Tissue'), ('', ''), ('Bed', 'ТОЛЬКО BED'), ('bed_type', 'Bed Type'), ('', ''), ('Stand', 'ТОЛЬКО STAND'), ('material', 'Material'), ('', ''), ('Basis', 'ТОЛЬКО BASIS')], max_length=32, verbose_name='Characteristic'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='property_en',
            field=models.CharField(max_length=64, verbose_name='Choice option (en)'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='property_gr',
            field=models.CharField(blank=True, max_length=64, verbose_name='Choice option (gr)'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='products', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='mattress',
            name='desc_en',
            field=models.TextField(verbose_name='Описание (gr)'),
        ),
        migrations.AlterField(
            model_name='mattresspad',
            name='desc_en',
            field=models.TextField(verbose_name='Описание (gr)'),
        ),
        migrations.AlterField(
            model_name='pillow',
            name='desc_en',
            field=models.TextField(verbose_name='Описание (gr)'),
        ),
        migrations.AlterField(
            model_name='size',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='size',
            name='discount',
            field=models.SmallIntegerField(default=0, verbose_name='Discount (%)'),
        ),
        migrations.AlterField(
            model_name='size',
            name='length',
            field=models.SmallIntegerField(default=200, verbose_name='Length'),
        ),
        migrations.AlterField(
            model_name='size',
            name='on_sale',
            field=models.BooleanField(default=False, verbose_name='On sale'),
        ),
        migrations.AlterField(
            model_name='size',
            name='priceEUR',
            field=models.SmallIntegerField(default=0, verbose_name='Price (euro)'),
        ),
        migrations.AlterField(
            model_name='size',
            name='product',
            field=models.CharField(blank=True, max_length=32, verbose_name='Product Name'),
        ),
        migrations.AlterField(
            model_name='size',
            name='width',
            field=models.SmallIntegerField(default=80, verbose_name='Width'),
        ),
        migrations.AlterField(
            model_name='stand',
            name='desc_en',
            field=models.TextField(verbose_name='Описание (gr)'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='collections',
            field=models.ManyToManyField(related_name='collection_stock', to='api.choice', verbose_name='Collections'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='desc_en',
            field=models.TextField(verbose_name='Description (en)'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='desc_gr',
            field=models.TextField(verbose_name='Description (gr)'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='discount',
            field=models.SmallIntegerField(default=0, verbose_name='Discount'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='expiry',
            field=models.DateField(verbose_name='Expiry'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='sizes',
            field=models.ManyToManyField(blank=True, related_name='sizes_stock', to='api.size', verbose_name='Sizes'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='desc_en',
            field=models.TextField(verbose_name='Desc (en)'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='desc_gr',
            field=models.TextField(verbose_name='Desc (gr)'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='name_en',
            field=models.CharField(max_length=32, unique=True, verbose_name='Name (en)'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='name_gr',
            field=models.CharField(blank=True, max_length=32, verbose_name='Name (gr)'),
        ),
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=64, unique=True, verbose_name='Video link'),
        ),
        migrations.DeleteModel(
            name='Marker',
        ),
    ]
