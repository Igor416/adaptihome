from rest_framework.serializers import Serializer, CharField, IntegerField
from . import models

class SearchResultSerializer(Serializer):
  link = CharField(max_length=64)
  text = CharField(max_length=64)
  
class CategoryResultSerializer(SearchResultSerializer):
  count = IntegerField()
  
  def to_representation(self, obj):
    return {
      'link': f'/catalog/{obj.name}/all',
      'text': getattr(obj, f'name_{obj}_pl'),
      'count': len(getattr(models, obj.name).objects.get_all())
    }
  
class ProductResultSerializer(SearchResultSerializer):
  price = IntegerField()
  discount = IntegerField()
  
  def to_representation(self, obj):
    return {
      'link': f'/product/{obj.category.name}/{obj.name}',
      'text': f'{getattr(obj.category, f"name_{self.lang}_s")}: {obj.name}',
      'price': obj.sizes.all()[0].price,
      'discount': obj.discount
    }