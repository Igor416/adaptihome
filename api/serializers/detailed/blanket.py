from api import models
from .product import DetailedProductSerializer

class BlanketSerializer(DetailedProductSerializer):
  class Meta(DetailedProductSerializer.Meta):
    model = models.Blanket