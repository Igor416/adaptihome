from django.db import models
from ..category import Category
from ..size import Size
from ..files import Image
from .. import managers

class Product(models.Model):
    name = models.CharField('Name', max_length=32, unique=True)
    desc_gr = models.TextField('Description (gr)')
    desc_en = models.TextField('Description (en)')
    discount = models.SmallIntegerField('Discount (%)', default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category', null=True)
    sizes = models.ManyToManyField(Size, related_name='sizes%(class)s', verbose_name='Sizes')
    shortcut = models.ForeignKey(Image, null=True, on_delete=models.SET_NULL, verbose_name='shortcut')
    images = models.ManyToManyField(Image, related_name='images%(class)s', verbose_name='Photos', blank=True)

    @classmethod
    def set_manager(cls):
        cls.objects = getattr(managers, cls.get_name() + 'Manager')(cls)

    @classmethod
    def get_name(cls):
        return cls.__name__

    def __str__(self):
        return f'{self._meta.verbose_name}: {self.name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.category:
            for size in self.sizes.all():
                if size.product == '' or not size.category:
                    size.set_product_and_category(self.name, self.category)
                    
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        abstract = True