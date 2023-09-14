from api import models
from .product import DetailedProductSerializer

class AccessorySerializer(DetailedProductSerializer):
  class Meta(DetailedProductSerializer.Meta):
    model = models.Accessory
    
  def to_representation(self, obj):
    r = super().to_representation(obj)
    return self.extract_lang('article', r)