from ..product import ProductSerializer
from api import models, catalog as ct
from ..choice import ChoiceSerializer
from ..files import ImageSerializer

class DetailedProductSerializer(ProductSerializer):
  class Meta:
      fields = '__all__'
      
  images = ImageSerializer(many=True)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for prop in filter(lambda prop: prop != 'rigidity', ct.get_all_props(self.Meta.model.get_name())):
        many = models.has_multiple_rels(self.Meta.model, prop)
        serializer = ChoiceSerializer(self.lang, many=many)
        self.fields.update({prop: serializer})

  def to_representation(self, obj):
    r = super().to_representation(obj)
    del r['id']
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
    
    from ..listed import getListedProductsSerializer
    r['suggestions'] = []
    for model in ct.get_suggestions(obj.get_name()):
        del r['suggestions_' + model]
    for model in ct.get_suggestions(obj.get_name()):
        for suggestion in getattr(obj, 'suggestions_' + model).all():
            serializer = getListedProductsSerializer(getattr(models, suggestion.get_name()), suggestion, lang=self.lang)
            r['suggestions'].append(serializer.data)
    return self.extract_lang('desc', r)