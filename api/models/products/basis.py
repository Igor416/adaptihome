from django.db import models
from .product import Product
from ..choice import Choice

class Basis(Product):
  distance = models.IntegerField(default=45)
  width = models.IntegerField(default=0)
  legs_height = models.IntegerField(default=0)

  recomended = models.ManyToManyField(Choice, related_name='recomendedBasis', verbose_name='Рекомендовано для матрассов')
  
  suggestions_Bed = models.ManyToManyField('Bed', blank=True)
  suggestions_Mattress = models.ManyToManyField('Mattress', blank=True)

  def __str__(self):
    return self._meta.verbose_name + ': ' + self.name