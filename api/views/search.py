from rest_framework.views import APIView, Response
from api import models, serializers
from api import catalog as ct
from .detectors import detect_lang

class SearchView(APIView):
  @detect_lang
  def post(self, request, lang):
    search = request.data
    categories_serializer = serializers.CategoryResultSerializer(self.search_categories(search, lang), lang=lang, many=True)

    products_data = []
    for queryset in self.search_products(search, lang):
      if queryset:
        products_data.extend(serializers.ProductResultSerializer(queryset, lang=lang, many=True).data)
    return Response({'categories': categories_serializer.data, 'products': products_data})
  
  def isearch(self, search, lang, objects):
    if lang == 'en':
      queryset = objects.filter(name_en_s__icontains=search)

    elif lang == 'gr':
      #sqllite3 doesn't support utf-8 search with insensitive case
      queryset = objects.filter(name_gr_s__contains=search.lower())
      queryset |= objects.filter(name_gr_s__contains=search.title())
      
    else:
      queryset = objects.filter(name__icontains=search)
      
    return queryset

  def search_categories(self, search, lang):
    return self.isearch(search, lang, models.Category.objects)

  def search_products(self, search, lang):
    for product_name in ct.get_all_categories():
      model = getattr(models, product_name)
      yield self.isearch(search, '', model.objects)