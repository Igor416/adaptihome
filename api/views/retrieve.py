from rest_framework.views import APIView, Response
from api import models, serializers
from .detectors import detect_lang

class ProductView(APIView):
  @detect_lang
  def get(self, request, lang, category, name):
    model = getattr(models, category)
    queryset = model.objects.get(name=name)
    serializer = getattr(serializers, model.get_name() + 'Serializer')(queryset, lang=lang)
    return Response(serializer.data)