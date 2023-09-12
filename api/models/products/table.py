from django.db import models
from .product import Product
from .relation_fields import m2m

class Table(Product):
  seats = models.IntegerField(default=0)
  depth = models.IntegerField(default=0)
  countertop_length = models.IntegerField(default=0)
  weight = models.IntegerField(default=0)
  countertop_weight = models.IntegerField(default=0)
  
  article_en = models.TextField('Article (gr)', blank=True)
  article_gr = models.TextField('Article (en)', blank=True)
  
  swivel_leg = m2m('swivel_leg')
  
  suggestions_Accessory = models.ManyToManyField('Accessory', blank=True)