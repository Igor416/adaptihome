from api import models
from .product import DetailedProductSerializer
from ..technologies import TechnologySerializer

class PillowSerializer(DetailedProductSerializer):
  class Meta(DetailedProductSerializer.Meta):
    model = models.Pillow
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['structure'] = TechnologySerializer(self.lang, many=True)