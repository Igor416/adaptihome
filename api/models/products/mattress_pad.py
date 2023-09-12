from django.db import models
from .product import Product
from ..technologies import Technology, LayerMattressPad
from .relation_fields import foreign_key, m2m

class MattressPad(Product):
  height = models.IntegerField(default=0)
  case = models.BooleanField(default=True)
  structure = models.ManyToManyField(Technology, through=LayerMattressPad, through_fields=('product', 'technology'), verbose_name='Структура')

  age = m2m('age', True)
  mattresspad_type = m2m('mattresspad_type')
  binding = foreign_key('binding')
  cover = m2m('cover', True)
  
  suggestions_Pillow = models.ManyToManyField('Pillow', blank=True)
  suggestions_Blanket = models.ManyToManyField('Blanket', blank=True)