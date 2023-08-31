# Generated by Django 4.1.1 on 2023-08-27 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0093_size_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=128, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, max_length=32, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, max_length=16, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping',
            field=models.CharField(choices=[('showroom', 'showroom'), ('courier', 'courier')], default='showroom', max_length=8, verbose_name='Shiiping Method'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sizes',
            field=models.ManyToManyField(blank=True, to='api.size', verbose_name='Picked Sizes'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.IntegerField(default=0, verbose_name='Total'),
        ),
    ]
