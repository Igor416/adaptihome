from .product import ListedProductsSerializer

def getListedProductsSerializer(_model, *args, **kwargs):
  class Meta:
    model = _model
    fields = ['name', 'discount', 'sizes', 'shortcut', 'category']
      
  return type(_model.get_name() + 'Serializer', (ListedProductsSerializer,), {'Meta': Meta})