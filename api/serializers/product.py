from .lang_detective import LangDetectiveSerializer
from .category import CategorySerializer
from .size import SizeSerializer
from .files import ImageSerializer

class ProductSerializer(LangDetectiveSerializer):
  sizes = SizeSerializer(many=True)
  shortcut = ImageSerializer()

  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['category'] = CategorySerializer(lang=self.lang)