from .import models
from . import catalog as ct

def isearch(search, lang, objects):
  if lang == 'en':
    queryset = objects.filter(name_en_s__icontains=search)

  elif lang == 'gr':
    #sqllite3 doesn't support utf-8 search with insensitive case
    queryset = objects.filter(name_gr_s__contains=search.lower())
    queryset |= objects.filter(name_gr_s__contains=search.title())
    
  else:
    queryset = objects.filter(name__icontains=search)
    
  return queryset

def search_categories(search, lang):
  return isearch(search, lang, models.Category.objects)

def search_products(search, lang):
  for product_name in ct.get_all_categories():
    model = getattr(models, product_name)
    yield isearch(search, '', model.objects)