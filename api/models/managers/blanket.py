from .product import ProductManager

class BlanketManager(ProductManager):
  def get_by_type(self, value):
    if value == 'all':
      return self.objs
    elif value == 'Thermoregulation':
      return self.get_by_names('YETI')
      
    return self.objs.filter(name__istartswith=value)