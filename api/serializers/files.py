from rest_framework.serializers import ModelSerializer
from api import models
      
class ImageSerializer(ModelSerializer):
  def to_representation(self, obj):
    return obj.get_absolute_url()
  
  class Meta:
    model = models.Image
    fields = ['image']