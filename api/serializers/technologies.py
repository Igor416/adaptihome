from api import models
from .lang_detective import LangDetectiveSerializer

class TechnologySerializer(LangDetectiveSerializer):
  class Meta:
    exclude = ['id']
    model = models.Technology

  def to_representation(self, obj):
    r = super().to_representation(obj)
    r['image'] = obj.get_absolute_url()
    return self.extract_lang('desc', self.extract_lang('name', r))