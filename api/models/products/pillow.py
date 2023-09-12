from django.db import models
from .product import Product
from ..technologies import Technology, LayerPillow
from .relation_fields import m2m

class Pillow(Product):
  height = models.IntegerField(default=0)
  case = models.BooleanField(default=True)
  structure = models.ManyToManyField(Technology, through=LayerPillow, through_fields=('product', 'technology'), verbose_name='Структура')

  age = m2m('age', True)
  material_filler = m2m('material_filler')
  cover = m2m('cover', True)
  
  suggestions_MattressPad = models.ManyToManyField('MattressPad', blank=True)
  suggestions_Blanket = models.ManyToManyField('Blanket', blank=True)