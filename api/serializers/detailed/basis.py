from api import models
from .product import DetailedProductSerializer
from ..choice import ChoiceSerializer

class BasisSerializer(DetailedProductSerializer):
  recomended = ChoiceSerializer(many=True)
  
  class Meta(DetailedProductSerializer.Meta):
    model = models.Basis