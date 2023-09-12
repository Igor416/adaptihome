from .product import ProductManager

class BedManager(ProductManager):
  def get_by_sleep_places(self, value):
    if value == 'one':
      return self.get_by_names('Chris', 'Alice', 'Mari')
    return self.objs.exclude(name__in={'Chris', 'Alice', 'Mari'})