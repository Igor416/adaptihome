from django.db import models
from . import create_related_field
from . import managers
from .category import Category
from .choice import Choice
from .size import Size
from .files import Image
from .technologies import Technology, LayerMattress, LayerPillow, LayerMattressPad

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
        abstract = True

class FoldingBed(Product):
    mattress_height = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    max_pressure = models.IntegerField(default=0)
    
    closed_dimensions = models.ManyToManyField(Size, related_name='closed_dimensions%(class)s', verbose_name='Closed Dimensions')
    table_dimensions = models.ManyToManyField(Size, related_name='table_dimensions%(class)s', verbose_name='Table Dimensions', blank=True)
    base = create_related_field('base')
    age = create_related_field('age', True, True)

class Bed(Product):
    headboard_height = models.IntegerField(default=0)
    extra_length = models.IntegerField(default=0)
    extra_width = models.IntegerField(default=0)

    bed_type = create_related_field('bed_type', '', True)
    
class Mattress(Product):
    height = models.IntegerField(default=0)
    springs = models.IntegerField(default=0)
    max_pressure = models.IntegerField(default=0)
    lifetime = models.IntegerField(default=10)
    case = models.BooleanField(default=True)
    structure = models.ManyToManyField(Technology, through=LayerMattress, through_fields=('product', 'technology'), verbose_name='Структура')
    
    mattress_type = create_related_field('mattress_type', '', True)
    age = create_related_field('age', True, True)
    rigidity1 = create_related_field('rigidity1', True)
    rigidity2 = create_related_field('rigidity2', True)
    collection = create_related_field('collection')
    springblock = create_related_field('springblock')
    construction = create_related_field('construction')
    
class Table(Product):
    depth = models.IntegerField(default=0)
    countertop_length = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    countertop_weight = models.IntegerField(default=0)

class Pillow(Product):
    height = models.IntegerField(default=0)
    case = models.BooleanField(default=True)
    structure = models.ManyToManyField(Technology, through=LayerPillow, through_fields=('product', 'technology'), verbose_name='Структура')

    age = create_related_field('age', True, True)
    material_filler = create_related_field('material_filler', '', True)
    cover = create_related_field('cover', True, True)

class MattressPad(Product):
    height = models.IntegerField(default=0)
    case = models.BooleanField(default=True)
    structure = models.ManyToManyField(Technology, through=LayerMattressPad, through_fields=('product', 'technology'), verbose_name='Структура')

    age = create_related_field('age', True, True)
    mattresspad_type = create_related_field('mattresspad_type', '', True)
    binding = create_related_field('binding')
    cover = create_related_field('cover', True, True)

class Blanket(Product):
    density = models.IntegerField(default=0)

    blanket_type = create_related_field('blanket_type', '', True)
    age = create_related_field('age', True, True)
    filling = create_related_field('filling', True, True)
    blanket_color = create_related_field('blanket_color')
    cover = create_related_field('cover', True, True)

class Basis(Product):
    distance = models.IntegerField(default=45)
    width = models.IntegerField(default=0)
    legs_height = models.IntegerField(default=0)

    recomended = models.ManyToManyField(Choice, related_name='recomendedBasis', verbose_name='Рекомендовано для матрассов')

    def __str__(self):
        return self._meta.verbose_name + ': ' + self.name

class Puff(Product):
    height = models.IntegerField(default=0)

    material = create_related_field('material', '', True)
