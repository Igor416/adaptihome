from rest_framework.serializers import Serializer
from api import models

class SearchResultSerializer(Serializer):
  def  __init__(self, *args, **kwargs):
    self.lang = kwargs.pop('lang', 'en')
    super().__init__(*args, **kwargs)
  
class CategoryResultSerializer(SearchResultSerializer):
  def to_representation(self, obj):
    return {
      'link': f'/shop/{obj.name.lower()}?order=low',
      'category': getattr(obj, f'name_{self.lang}_pl'),
      'count': len(getattr(models, obj.name).objects.get_all())
    }
  
class ProductResultSerializer(SearchResultSerializer):
  def to_representation(self, obj):
    return {
      'link': f'/product/{obj.category.name.lower()}/{obj.name}',
      'category': getattr(obj.category, f"name_{self.lang}_s"),
      'name': obj.name,
      'price': obj.sizes.all()[0].price,
      'discount': obj.discount
    }