from django.db.models import Manager
from api import catalog as ct
from .category import Category
from .choice import Choice

class ProductManager(Manager):
  def __init__(self, model, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.model = model
    self.category = Category.objects.get(name=self.model.get_name())
    self.objs = model.objects.all()

  def get_all(self):
    return self.objs.all()

  def get_filtered(self, filter):
    queryset = self.objs
    for key, values in filter.items():
      if key in ['order', 'category']:
        continue
      part = self.objs.none()
      
      for value in values.split(','):
        try:
          part |= getattr(self, 'get_by_' + ('type' if key == self.model.get_name() else key))(value)
        except AttributeError:
          continue
        
      queryset &= part

    order = filter.get('order')
    table = {
      'a': 'name',
      'z': '-name'
    }
    if order in table:
      return queryset.order_by(table[order])
    
    return queryset

  def get_by_names(self, *names):
    queryset = self.objs.none()

    for obj in names:
      queryset |= self.objs.filter(name=obj)

    return queryset

  def get_prop(self, name, property):
    property = property.replace('_', ' ').title()
    if len(property.split(' ')) > 1:
      return Choice.objects.get(name=name, property_en=property)
    
    return Choice.objects.get(name=name, property_en=property)
      
  def get_by_age(self, value):
    try:
      age = self.get_prop(ct.AGE, value)
      return self.objs.filter(age=age)
    except:
      return self.objs.none()

class FoldingBedManager(ProductManager):
  def get_by_type(self, key):
    if key == 'All beds':
      queryset = self.get_all()

    return queryset
  
class BedManager(ProductManager):
  def get_by_sleep_places(self, value):
    if value == 'one':
      return self.get_by_names('Chris', 'Alice', 'Mari')
    return self.objs.exclude(name__in={'Chris', 'Alice', 'Mari'})

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

class TableManager(ProductManager):
  pass

class PillowManager(ProductManager):
  def get_by_type(self, value):
    if value == 'all':
      return self.objs
    
    if value == 'latex':
      material_filler = self.get_prop(ct.MATERIAL_FILLER, 'Latex Monolith')
    elif value == 'memory_foam':
      material_filler = self.get_prop(ct.MATERIAL_FILLER, 'MemoryFoam Slices')

    return self.objs.filter(material_filler=material_filler)

class MattressPadManager(ProductManager):
  def get_by_type(self, value):
    if value == 'all':
      return self.objs
    return self.objs.filter(mattresspad_type=self.get_prop(ct.MATTRESSPAD_TYPE, value))

class BlanketManager(ProductManager):
  def get_by_type(self, value):
    if value == 'all':
      return self.objs
    elif value == 'Thermoregulation':
      return self.get_by_names('YETI')
      
    return self.objs.filter(name__istartswith=value)

class BasisManager(ProductManager):
  pass

class PuffManager(ProductManager):
  pass

class AccessoryManager(ProductManager):
  pass