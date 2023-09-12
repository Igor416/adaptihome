from .product import ProductManager
from ..choice import Choice
from api import catalog as ct

class MattressManager(ProductManager):
  def get_by_collection(self, value):
    collection = self.get_prop(ct.COLLECTION, value)
    return self.objs.filter(collection=collection)

  def get_by_rigidity(self, value):
    if value == 'latex':
      return self.get_by_names('F2', 'F5', 'M1', 'M3', 'M4', 'M5', 'X2', 'X3', 'X4', 'X6', 'X7', 'X8')
      
    elif value == 'coconut_coir':
      return self.get_by_names('F1', 'F3', 'F5', 'M3', 'M4', 'X5', 'X6', 'X7', 'L2', 'L3', 'L6')

    elif value == 'memory_effect':
      return self.get_by_names('F6', 'M2', 'X1', 'A5')

    elif value == 'non-symmetrical':
      queryset = self.objs.none()
      for rigidity1 in Choice.objects.filter(name=ct.RIGIDITY):
        for obj in self.objs.filter(rigidity1=rigidity1):
          if obj.rigidity2 is None:
            continue
          elif obj.rigidity2.property_en == rigidity1.property_en:
            queryset |= self.objs.filter(name=obj.name)
      return queryset
    else:
      rigidity1 = self.get_prop(ct.RIGIDITY, value)
      rigidity2 = self.get_prop(ct.RIGIDITY, value)

      return self.objs.filter(rigidity1=rigidity1) | self.objs.filter(rigidity2=rigidity2)