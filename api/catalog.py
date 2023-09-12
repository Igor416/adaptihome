#Categories
FOLDINGBED = 'FoldingBed'
BED = 'Bed'
MATTRESS = 'Mattress'
TABLE = 'Table'
PILLOW = 'Pillow'
MATTRESSPAD = 'MattressPad'
BLANKET = 'Blanket'
BASIS = 'Basis'
PUFF = 'Puff'
ACCESSORY = 'Accessory'

#Properties
MATTRESS_HEIGHT = 'mattress_height'
HEIGHT = 'height'
MAX_PRESSURE = 'max_pressure'
LAMELS = 'lamels'
HEADBOARD_HEIGHT = 'headboard_height'
EXTRA_LENGTH = 'extra_length'
EXTRA_WIDTH = 'extra_width'
HEIGHT = 'height'
SPRINGS = 'springs'
LIFETIME = 'lifetime'
CASE = 'case'
DEPTH = 'depth'
COUNTERTOP_LENGTH = 'countertop_length'
WEIGHT = 'weight'
COUNTERTOP_WEIGHT = 'countertop_weight'
DENSITY = 'density'
DISTANCE = 'distance'
WIDTH = 'width'
LEGS_HEIGHT = 'legs_height'
RECOMENDED = 'recomended'

#Choices
BASE = 'base'
AGE = 'age'
WALL = 'wall'
LEGS = 'legs'
CUSHION = 'cushion'
BED_TYPE = 'bed_type'
MATTRESS_TYPE = 'mattress_type'
COLLECTION = 'collection'
CONSTRUCTION = 'construction'
RIGIDITY = 'rigidity'
SPRINGBLOCK = 'springblock'
MATERIAL_FILLER = 'material_filler'
COVER = 'cover'
MATTRESSPAD_TYPE = 'mattresspad_type'
BINDING = 'binding'
BLANKET_TYPE = 'blanket_type'
BLANKET_COLOR = 'blanket_color'
FILLING = 'filling'
MATERIAL = 'material'

COMMON_PROPERTIES  = {
  AGE: [FOLDINGBED, MATTRESS, PILLOW, BLANKET, MATTRESSPAD],
  RIGIDITY: [MATTRESS, MATTRESSPAD],
  COVER: [PILLOW, MATTRESSPAD, BLANKET]
}

CATALOG = {
  FOLDINGBED: [BASE, WALL, LEGS, CUSHION],
  BED: [BED_TYPE],
  MATTRESS: [MATTRESS_TYPE, COLLECTION, CONSTRUCTION, RIGIDITY, SPRINGBLOCK],
  TABLE: [],
  PILLOW: [MATERIAL_FILLER],
  MATTRESSPAD: [MATTRESSPAD_TYPE, RIGIDITY, BINDING],
  BLANKET: [BLANKET_TYPE, BLANKET_COLOR, FILLING],
  BASIS: [],
  PUFF: [MATERIAL],
  ACCESSORY: []
}

ORDER = {
  FOLDINGBED: (AGE, WALL, MATTRESS_HEIGHT, BASE, LAMELS, HEIGHT, MAX_PRESSURE, LEGS, CUSHION),
  BED: (BED_TYPE, HEADBOARD_HEIGHT, EXTRA_LENGTH, EXTRA_WIDTH),
  MATTRESS: (MATTRESS_TYPE, AGE, HEIGHT, MAX_PRESSURE, RIGIDITY + '1', RIGIDITY + '2', SPRINGS, LIFETIME, COLLECTION, SPRINGBLOCK, CONSTRUCTION, CASE),
  TABLE: (),
  PILLOW: (AGE, MATERIAL_FILLER, HEIGHT, CASE, COVER),
  MATTRESSPAD: (AGE, MATTRESSPAD_TYPE, HEIGHT, CASE, BINDING, COVER),
  BLANKET: (BLANKET_TYPE, AGE, FILLING, DENSITY, COVER, BLANKET_COLOR),
  BASIS: (DISTANCE, WIDTH, LEGS_HEIGHT, RECOMENDED),
  PUFF: (HEIGHT, MATERIAL),
  ACCESSORY: ()
}

SUGGESTIONS = {
  FOLDINGBED: [MATTRESS, PUFF],
  BED: [MATTRESS, PUFF],
  MATTRESS: [PILLOW, MATTRESSPAD],
  TABLE: [ACCESSORY],
  PILLOW: [MATTRESSPAD, BLANKET],
  MATTRESSPAD: [PILLOW, BLANKET],
  BLANKET: [PILLOW, MATTRESSPAD],
  BASIS: [BED, MATTRESS],
  PUFF: [FOLDINGBED],
  ACCESSORY: [ACCESSORY]
}

from .translations import EN
def get_all_categories():
  return list(CATALOG.keys())
      
def get_all_props(product):
  return CATALOG[product] + [prop for prop, prs in COMMON_PROPERTIES.items() if product in prs]

def get_categories(property):
  categories = COMMON_PROPERTIES.get(property)
  if not categories:
    for pr, props in CATALOG.items():
      if property in props:
        return [pr]
  return categories

def get_pr_trans(product, lang=EN, plural=False):
  from .translations import langs, products
  if isinstance(lang, str):
    lang = langs.index(lang)
  return products.get(product)[lang][int(plural)]

def get_prop_trans(property, lang=EN):
  from .translations import langs, properties, choices
  if isinstance(lang, str):
    lang = langs.index(lang)
  return (properties.get(property) or choices.get(property))[lang]

def get_order(model):
  return ORDER[model]

def get_suggestions(model):
  return SUGGESTIONS[model]

def get_pr_choices():
  return [(key, get_pr_trans(key)) for key in CATALOG.keys()]

def get_prop_choices():
  choices = [
    ('COMMON', 'COMMON')
  ]

  for prop in COMMON_PROPERTIES.keys():
    choices.append((prop, get_prop_trans(prop)))

  for pr, props in CATALOG.items():
    if pr == BASIS:
      continue
    choices.append(('', ''))
    choices.append((pr, 'ONLY ' + get_pr_trans(pr).upper()))
    for prop in props:
      choices.append((prop, get_prop_trans(prop)))
  return choices