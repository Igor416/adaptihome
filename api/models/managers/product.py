from django.db.models import Manager, Min, F
from ..choice import Choice
from api import catalog as ct

class ProductManager(Manager):
  def __init__(self, model, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.model = model
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
      'z': '-name',
      'low': 'cheapest',
      'high': '-cheapest'
    }
    if order in table:
      if table[order].endswith('cheapest'):
        queryset = queryset.annotate(cheapest=Min(F('sizes__price')))
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