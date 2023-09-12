from django.db import models
from .product import Product
from .relation_fields import m2m

class Puff(Product):
  height = models.IntegerField(default=0)

  material = m2m('material')
  
  suggestions_FoldingBed = models.ManyToManyField('FoldingBed', blank=True)