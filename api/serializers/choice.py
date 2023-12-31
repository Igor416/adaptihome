from api import models
from .lang_detective import LangDetectiveSerializer

class ChoiceSerializer(LangDetectiveSerializer):
  class Meta:
      exclude = ['name', 'category']
      model = models.Choice

  def to_representation(self, obj):
      return getattr(obj, 'property_' + self.lang)