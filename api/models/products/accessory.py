from django.db import models
from .product import Product

class Accessory(Product):
  article_en = models.TextField('Article (en)', blank=True)
  article_gr = models.TextField('Article (gr)', blank=True)
  
  suggestions_Accessory = models.ManyToManyField('self', blank=True)