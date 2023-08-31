from rest_framework.serializers import ModelSerializer, IntegerField
from api import models
from api import catalog
from api.translations import langs

class LangDetectiveSerializer(ModelSerializer):
  def  __init__(self, *args, **kwargs):
    self.lang = kwargs.pop('lang', 'en')
    super().__init__(*args, **kwargs)
      
  def extract_lang(self, name, r):
    for lang in langs:
      if lang == self.lang:
        r.update({
            name: r.pop(name + '_' + lang),
        })
        continue
      r.pop(name + '_' + lang)
    return r

from .search import CategoryResultSerializer, ProductResultSerializer
from .size import SizeSerializer
from .mattres_collection_price import MattressColectionsPriceSerializer
from .products_factory import ListedProductsSerializerFactory, DetailedProductSerializerFactory
from .order import OrderSerializer