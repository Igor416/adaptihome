from api import models
from .product import DetailedProductSerializer

class PuffSerializer(DetailedProductSerializer):
  class Meta(DetailedProductSerializer.Meta):
    model = models.Puff