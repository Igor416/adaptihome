from . import models, catalog as ct, LangDetectiveSerializer

class CategorySerializer(LangDetectiveSerializer):
  class Meta:
    fields = '__all__'
    model = models.Category

  def to_representation(self, obj):
    return {
      'name': obj.name,
      'name_s': getattr(obj, f'name_{self.lang}_s'),
      'name_pl': getattr(obj, f'name_{self.lang}_pl'),
    }