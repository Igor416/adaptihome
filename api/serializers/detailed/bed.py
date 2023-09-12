from api import models
from .product import DetailedProductSerializer

class BedSerializer(DetailedProductSerializer):
  class Meta(DetailedProductSerializer.Meta):
    model = models.Bed