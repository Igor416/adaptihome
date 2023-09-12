from django.db import models
from .product import Product
from ..technologies import Technology, LayerMattress
from .relation_fields import foreign_key, m2m

class Mattress(Product):
  height = models.IntegerField(default=0)
  springs = models.IntegerField(default=0)
  max_pressure = models.IntegerField(default=0)
  lifetime = models.IntegerField(default=10)
  case = models.BooleanField(default=True)
  structure = models.ManyToManyField(Technology, through=LayerMattress, through_fields=('product', 'technology'), verbose_name='Структура')
  
  mattress_type = m2m('mattress_type')
  age = m2m('age', True)
  rigidity1 = foreign_key('rigidity1', True)
  rigidity2 = foreign_key('rigidity2', True)
  collection = foreign_key('collection')
  springblock = foreign_key('springblock')
  construction = foreign_key('construction')
  
  suggestions_Pillow = models.ManyToManyField('Pillow', blank=True)
  suggestions_MattressPad = models.ManyToManyField('MattressPad', blank=True)