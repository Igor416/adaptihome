from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import CategoryResultSerializer, ProductResultSerializer, MattressColectionsPriceSerializer
from .serializers import ListedProductsSerializerFactory, DetailedProductSerializerFactory
from .detectors import detect_lang
from .search import search_categories, search_products
from . import models
from requests import get
import json

class SearchView(APIView):
    @detect_lang
    def post(self, request, lang):
        search = request.data['search']
        categories_serializer = CategoryResultSerializer(search_categories(search, lang), lang=lang, many=True)

        products_data = []
        for queryset in search_products(search, lang):
            products_data.append(ProductResultSerializer(queryset, lang=lang, many=True))

        return Response({'categories': categories_serializer.data, 'products': products_data})

class MattressColectionsPriceView(APIView):
    def get(self, request, country):
        queryset = models.Choice.objects.filter(name='collection')
        serializer = MattressColectionsPriceSerializer(queryset, many=True)
        return Response(serializer.data)

class ListedProductsView(APIView):
    @detect_lang
    def get(self, request, lang, category):
        category = ''.join([part.title() for part in category.split('_')])
        model = getattr(models, category)
        if isinstance(model, list):
            accessories = []
            for product in models.Accessories:
                if request.query_params.get(product.get_name().lower(), None):
                    accessories = [product]
                    break
            else:
                for product in request.query_params.get('category', 'all').split(','):
                    if product == 'all':
                        accessories = model
                        break
                    else:
                        accessories.append(getattr(models, ''.join([part.title() for part in product.split('_')])))
            resp = []
            for model in accessories:
                resp.extend(self.get_response_data(model, lang, request.query_params))
            return Response(self.sort_by_price(resp, request.query_params))
        return Response(self.sort_by_price(self.get_response_data(model, lang, request.query_params), request.query_params))
    
    def get_response_data(self, model, lang, filters):
        queryset = model.objects.get_filtered(filters)
        serializer = ListedProductsSerializerFactory(model, lang).create(queryset, lang=lang, many=True)
        return serializer.data
    
    def sort_by_price(self, resp, query_params):
        if query_params.get('order') not in ['low', 'high']:
            return resp
        
        print(len(resp))
        discount = lambda entry: entry['sizes'][0]['discount'] if entry['sizes'][0]['discount'] > entry['discount'] else entry['discount']
        
        return sorted(resp, key=lambda entry: entry['sizes'][0]['price'] * (100 - discount(entry) / 100), reverse=query_params.get('order') == 'high')

class DetailedProductView(APIView):
    @detect_lang
    def get(self, request, lang, category, name):
        model = getattr(models, category)
        queryset = model.objects.get(name=name)
        serializer = DetailedProductSerializerFactory(model, lang).create(queryset, lang=lang)
        return Response(serializer.data)
    
class WorkerView(APIView):
    def get(self, request):
        categories = ['folding_bed', 'bed', 'mattress', 'table', 'accessories', 'puff']
        lengths = dict()
        for category in categories:
            category = ''.join([part.title() for part in category.split('_')])
            model = getattr(models, category)
            if isinstance(model, list):
                accessories = model
                resp = 0
                for model in accessories:
                    resp += len(model.objects.all())
                lengths[category] = resp
            else:
                queryset = model.objects.all()
                lengths[category] = len(queryset)
        return Response(lengths)
        