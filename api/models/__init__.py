from django.db import models
from api import catalog
from api.translations import GR, EN

def save_langs(val_gr, val_en):
	val_en = val_en.strip()
	if val_gr == '':
		val_gr = val_en
	else:
		val_gr = val_gr.strip()

	return val_gr, val_en

def has_multiple_rels(model, field):
	if field == 'rigidity':
		return False
	return hasattr(getattr(model, field), 'rel')

from .category import Category
from .choice import Choice
from .size import Size
from .files import Image
from .technologies import Technology, LayerMattress, LayerPillow, LayerMattressPad
from .products import FoldingBed, Bed, Mattress, Table, Pillow, MattressPad, Blanket, Basis, Puff, Accessory
from .order import Order, OrderedSize

Accessories = [Pillow, MattressPad, Blanket, Basis, Accessory]