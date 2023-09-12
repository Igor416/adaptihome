from api import models
from .product import DetailedProductSerializer

class AccessorySerializer(DetailedProductSerializer):
  class Meta(DetailedProductSerializer.Meta):
    model = models.Accessory