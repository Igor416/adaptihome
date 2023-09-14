from django.db import models
from .product import Product
from .relation_fields import m2m, foreign_key
from ..size import Size

class Table(Product):
  seats = models.IntegerField(default=0)
  countertop_length = models.IntegerField(default=0)
  weight = models.IntegerField(default=0)
  countertop_weight = models.IntegerField(default=0)
  
  article_en = models.TextField('Article (en)', blank=True)
  article_gr = models.TextField('Article (gr)', blank=True)
  
  dimensions = models.ForeignKey(Size, null=True, on_delete=models.SET_NULL, related_name='dimensions', verbose_name='Dimensions')
  
  swivel_leg = m2m('swivel_leg')
  fixation = foreign_key('fixation')
  
  suggestions_Accessory = models.ManyToManyField('Accessory', blank=True)