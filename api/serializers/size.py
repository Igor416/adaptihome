from api import models
from rest_framework.serializers import ModelSerializer, IntegerField

class SizeSerializer(ModelSerializer):
  quantity = IntegerField(default=1)
  
  class Meta:
    exclude = ['id', 'category']
    model = models.Size