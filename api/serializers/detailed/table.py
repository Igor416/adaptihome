from api import models
from .product import DetailedProductSerializer

class TableSerializer(DetailedProductSerializer):
  class Meta(DetailedProductSerializer.Meta):
    model = models.Table
    
  def to_representation(self, obj):
    r = super().to_representation(obj)
    r['dimensions'] = {
      'closed': [74, obj.dimensions.width, obj.dimensions.length]
    }
    for i in range(1, obj.seats // 2 -1):
      r['dimensions'].update({
        f'worktop_{i}': [74, obj.dimensions.width, obj.dimensions.length + obj.countertop_length * i]
      })
    r['dimensions'].update({
      'thickness': 18
    })
    return self.extract_lang('article', r)