from django.db import models
from .product import Product
from .relation_fields import foreign_key, m2m

class Blanket(Product):
  density = models.IntegerField(default=0)

  blanket_type = m2m('blanket_type')
  age = m2m('age', True)
  filling = m2m('filling', True)
  blanket_color = foreign_key('blanket_color')
  cover = m2m('cover', True)
  
  suggestions_Pillow = models.ManyToManyField('Pillow', blank=True)
  suggestions_MattressPad = models.ManyToManyField('MattressPad', blank=True)