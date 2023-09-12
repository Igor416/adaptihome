from api import models
from .product import DetailedProductSerializer

class FoldingBedSerializer(DetailedProductSerializer):
  class Meta(DetailedProductSerializer.Meta):
    model = models.FoldingBed
    
  def to_representation(self, obj):
    r = super().to_representation(obj)
    del r['closed_dimensions']
    del r['table_dimensions']
    r['dimensions'] = {
      'closed': [obj.closed_dimensions.length, obj.closed_dimensions.width, 410],
      'clear': [obj.closed_dimensions.length, obj.closed_dimensions.width, 2185],
      'mattress_height': obj.mattress_height,
      'sidewall': 36,
      'top_panel': 36,
      'bottom_panel': 36,
      'back' : 18,
      'facades': 18
    }
    if obj.table_dimensions:
      r['dimensions'].update({
        'table': [obj.table_dimensions.length, obj.table_dimensions.width],
        'table_panel': 18
      })
    return self.extract_lang('article', r)