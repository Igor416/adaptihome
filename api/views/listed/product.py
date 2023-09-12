from rest_framework.generics import ListAPIView
from api import serializers
from ..detectors import detect_lang

class ProductView(ListAPIView):
  def get_queryset(self):
    return self.model.objects.get_filtered(self.request.query_params)
  
  def get_serializer(self, instance=None, data=None, many=False, partial=False):
    return serializers.getListedProductsSerializer(self.model)(instance, many=many, lang=self.get_lang())
  
  def get_lang(self):
    func = lambda self, request, lang: lang
    return detect_lang(func)(self, self.request)