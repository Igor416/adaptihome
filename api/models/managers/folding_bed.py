from .product import ProductManager

class FoldingBedManager(ProductManager):
  def get_by_type(self, key):
    if key == 'All beds':
      queryset = self.get_all()

    return queryset