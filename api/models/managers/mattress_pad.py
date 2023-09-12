from .product import ProductManager
from api import catalog as ct

class MattressPadManager(ProductManager):
  def get_by_type(self, value):
    if value == 'all':
      return self.objs
    return self.objs.filter(mattresspad_type=self.get_prop(ct.MATTRESSPAD_TYPE, value))