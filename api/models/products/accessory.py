from django.db import models
from .product import Product

class Accessory(Product):
  suggestions_Accessory = models.ManyToManyField('self', blank=True)