from . import models, ModelSerializer

class SizeSerializer(ModelSerializer):
  class Meta:
    exclude = ['id', 'category', 'product']
    model = models.Size
    
  def to_representation(self, obj):
    r = super().to_representation(obj)
    r['quantity'] = 1
    return r