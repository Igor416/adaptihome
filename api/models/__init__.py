from django.db import models
from api import catalog
from api.translations import GR, EN

def create_related_field(prop, multiple=False, plural=False):
	kwargs = {
		'to': 'Choice',
		'related_name': prop + ('%(class)s' if multiple else '')
	}

	if plural:
		field = models.ManyToManyField
	else:
		field = models.ForeignKey
		kwargs.update({'on_delete': models.SET_NULL, 'null': True})

	return field(**kwargs)

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
from .products import FoldingBed, Bed, Mattress, Table, Pillow, MattressPad, Blanket, Basis, Puff

Accessories = [Pillow, MattressPad, Blanket, Basis]