from django.db.models import ForeignKey, SET_NULL, ManyToManyField

def foreign_key(prop, multiple=False):
	kwargs = {
		'to': 'Choice',
		'related_name': prop + ('%(class)s' if multiple else ''),
		'on_delete': SET_NULL,
		'null': True
	}
	return ForeignKey(**kwargs)

def m2m(prop, multiple=False):
	kwargs = {
		'to': 'Choice',
		'related_name': prop + ('%(class)s' if multiple else '')
	}
	return ManyToManyField(**kwargs)