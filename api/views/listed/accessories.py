from rest_framework.views import APIView, Response
from api import models, serializers
from ..detectors import detect_lang

class AccessoriesView(APIView):
    @detect_lang
    def get(self, request, lang):
      accessories = []
      for product in models.Accessories:
        if request.query_params.get(product.get_name(), None):
          accessories = [product]
          break
      else:
        for product in request.query_params.get('category', 'all').split(','):
          if product == 'all':
            accessories = models.Accessories
            break
          accessories.append(getattr(models, product))
      resp = []
      for model in accessories:
        queryset = model.objects.get_filtered(request.query_params)
        serializer_class = serializers.getListedProductsSerializer(model)
        serializer = serializer_class(queryset, lang=lang, many=True)
        resp.extend(serializer.data)
      return Response(resp)