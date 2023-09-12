from rest_framework.generics import ListAPIView
from api import models, serializers

class MattressColectionsPriceView(ListAPIView):
  queryset = models.Choice.objects.filter(name='collection')
  serializer_class = serializers.MattressColectionsPriceSerializer