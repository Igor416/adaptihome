from rest_framework.views import APIView, Response
from api import models, serializers
from .detectors import detect_lang

class OrderView(APIView):
  @detect_lang
  def get(self, request, lang, id):
    order = models.Order.objects.get(id=id)
    return Response(serializers.OrderSerializer(order, lang=lang).data)
  
  @detect_lang
  def post(self, request, lang, id):
    serializer = serializers.OrderSerializer(data=self.extract_sizes(request), lang=lang)
    if serializer.is_valid():
      serializer.save()
        
    return Response(serializer.data)
  
  @detect_lang
  def patch(self, request, lang, id):
    order = models.Order.objects.get(id=id)
    serializer = serializers.OrderSerializer(order, data=self.extract_sizes(request), lang=lang)
    if serializer.is_valid():
      serializer.save()
      
    return Response(serializer.data)
  
  @staticmethod
  def extract_sizes(request):
    sizes = []
    for product in request.data.pop('products'):
      for size in product['sizes']:
        sizes.append(size)
            
    request.data.update({'sizes': sizes})
    return request.data