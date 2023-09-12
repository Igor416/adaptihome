from api import models
from .product import DetailedProductSerializer

class TableSerializer(DetailedProductSerializer):
  class Meta(DetailedProductSerializer.Meta):
    model = models.Table