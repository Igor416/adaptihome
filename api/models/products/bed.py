from django.db import models
from .product import Product
from .relation_fields import m2m

class Bed(Product):
  headboard_height = models.IntegerField(default=0)
  extra_length = models.IntegerField(default=0)
  extra_width = models.IntegerField(default=0)

  bed_type = m2m('bed_type')
  
  suggestions_Mattress = models.ManyToManyField('Mattress', blank=True)
  suggestions_Puff = models.ManyToManyField('Puff', blank=True)