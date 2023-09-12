from api import models
from .product import DetailedProductSerializer
from ..technologies import TechnologySerializer
from ..choice import ChoiceSerializer

class MattressSerializer(DetailedProductSerializer):
  class Meta(DetailedProductSerializer.Meta):
    model = models.Mattress
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['structure'] = TechnologySerializer(self.lang, many=True)
    self.fields.update({
      'rigidity1': ChoiceSerializer(self.lang),
      'rigidity2': ChoiceSerializer(self.lang)
    })