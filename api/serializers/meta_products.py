from rest_framework.serializers import SerializerMethodField
from . import models, catalog as ct, LangDetectiveSerializer
from .category import CategorySerializer
from .size import SizeSerializer
from .files import ImageSerializer

class ProductSerializer(LangDetectiveSerializer):
    sizes = SizeSerializer(many=True)
    shortcut = ImageSerializer()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'] = CategorySerializer(lang=self.lang)

    def to_representation(self, obj):
        r = super().to_representation(obj)
        r['sizes'] = sorted(r['sizes'], key=lambda size: size['price'] * (100 - size['discount']) / 100)
        return r

class ListedProductsSerializer(ProductSerializer):
    desc = SerializerMethodField()

    def get_desc(self, obj):
        shortened, symbols, words = '', 288, 0
        for sent in getattr(obj, 'desc_' + self.lang).split('.'):
            words += len(sent.strip())
            if words <= symbols:
                shortened += sent + '. '
            else:
                return shortened
        else:
            return getattr(obj, 'desc_' + self.lang)

    def to_representation(self, obj):
        r = super().to_representation(obj)
        r['sizes'] = [r['sizes'][0]]
        return r

class DetailedProductSerializer(ProductSerializer):
    images = ImageSerializer(many=True)

    def to_representation(self, obj):
        r = super().to_representation(obj)
        del r['id']
        for model in ct.get_suggestions(obj.get_name()):
            del r['suggestions_' + model]
            
        r['suggestions'] = []
        r['characteristic'] = {}
        r['images'].insert(0, r['shortcut'])
        order = ct.get_order(obj.get_name())
        for key in order:
            if key.startswith('rigidity'):
                key_lang = ct.get_prop_trans(key[:-1], self.lang) + f' {key[-1]}'
            else:
                key_lang = ct.get_prop_trans(key, self.lang)
            
            r['characteristic'][key_lang] = r[key] if key.startswith('extra') else r.pop(key)

        for size in [*r['sizes']]:
            if size['length'] == 200:
                new_size = size.copy()
                new_size['length'] = 190
                r['sizes'].append(new_size)
        
        from .products_factory import ListedProductsSerializerFactory
        for model in ct.get_suggestions(obj.get_name()):
            for suggestion in getattr(obj, 'suggestions_' + model).all():
                serializer = ListedProductsSerializerFactory(getattr(models, suggestion.get_name()), self.lang).create(suggestion, lang=self.lang)
                r['suggestions'].append(serializer.data)
        return self.extract_lang('desc', r)