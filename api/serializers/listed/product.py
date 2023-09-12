from rest_framework.serializers import SerializerMethodField
from ..product import ProductSerializer
from ..size import SizeSerializer

class ListedProductsSerializer(ProductSerializer):
  desc = SerializerMethodField()
  sizes = SerializerMethodField()

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

  def get_sizes(self, obj):
    return [SizeSerializer(instance=obj.sizes.first()).data]