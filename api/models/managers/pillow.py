from .product import ProductManager
from api import catalog as ct

class PillowManager(ProductManager):
  def get_by_type(self, value):
    if value == 'all':
      return self.objs
    
    if value == 'latex':
      material_filler = self.get_prop(ct.MATERIAL_FILLER, 'Latex Monolith')
    elif value == 'memory_foam':
      material_filler = self.get_prop(ct.MATERIAL_FILLER, 'MemoryFoam Slices')

    return self.objs.filter(material_filler=material_filler)