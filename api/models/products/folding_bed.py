from django.db import models
from .product import Product
from ..size import Size
from .relation_fields import foreign_key, m2m

class FoldingBed(Product):
  mattress_height = models.IntegerField(default=0)
  height = models.IntegerField(default=0)
  max_pressure = models.IntegerField(default=0)
  lamels = models.IntegerField(default=0)
  
  article_en = models.TextField('Article (en)', blank=True)
  article_gr = models.TextField('Article (gr)', blank=True)
  
  closed_dimensions = models.ForeignKey(Size, null=True, on_delete=models.SET_NULL, related_name='closed_dimensions', verbose_name='Closed Dimensions')
  table_dimensions = models.ForeignKey(Size, null=True, on_delete=models.SET_NULL, related_name='table_dimensions', verbose_name='Table Dimensions', blank=True)
  
  base = foreign_key('base')
  age = m2m('age', True)
  wall = m2m('wall')
  legs = foreign_key('legs')
  cushion = foreign_key('cushion')
  
  suggestions_Mattress = models.ManyToManyField('Mattress', blank=True)
  suggestions_Puff = models.ManyToManyField('Puff', blank=True)