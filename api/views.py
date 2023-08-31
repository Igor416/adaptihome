from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategoryResultSerializer, ProductResultSerializer, MattressColectionsPriceSerializer, OrderSerializer
from .serializers import ListedProductsSerializerFactory, DetailedProductSerializerFactory
from .detectors import detect_lang
from .search import search_categories, search_products
from . import models

class SearchView(APIView):
    @detect_lang
    def post(self, request, lang):
        search = request.data
        categories_serializer = CategoryResultSerializer(search_categories(search, lang), lang=lang, many=True)

        products_data = []
        for queryset in search_products(search, lang):
            if queryset:
                products_data.extend(ProductResultSerializer(queryset, lang=lang, many=True).data)
        return Response({'categories': categories_serializer.data, 'products': products_data})

class MattressColectionsPriceView(ListAPIView):
    queryset = models.Choice.objects.filter(name='collection')
    serializer_class = MattressColectionsPriceSerializer

class ListProductView(APIView):
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
        
        discount = lambda entry: entry['sizes'][0]['discount'] if entry['sizes'][0]['discount'] > entry['discount'] else entry['discount']
        
        return sorted(resp, key=lambda entry: entry['sizes'][0]['price'] * (100 - discount(entry) / 100), reverse=query_params.get('order') == 'high')

class RetrieveProductView(APIView):
    @detect_lang
    def get(self, request, lang, category, name):
        category = ''.join([part.title() for part in category.split('_')])
        model = getattr(models, category)
        queryset = model.objects.get(name=name)
        serializer = DetailedProductSerializerFactory(model, lang).create(queryset, lang=lang)
        return Response(serializer.data)

class OrderView(APIView):
    @detect_lang
    def get(self, request, lang, id):
        order = models.Order.objects.get(id=id)
        return Response(OrderSerializer(order, lang=lang).data)
    
    @detect_lang
    def post(self, request, lang, id):
        serializer = OrderSerializer(data=self.extract_sizes(request), lang=lang)
        if serializer.is_valid():
            serializer.save()
            
        return Response(serializer.data)
    
    @detect_lang
    def patch(self, request, lang, id):
        order = models.Order.objects.get(id=id)
        serializer = OrderSerializer(order, data=self.extract_sizes(request), lang=lang)
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