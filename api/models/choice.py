from django.db import models
from . import save_langs, catalog as ct
from .category import Category

class Choice(models.Model):
	choices = ct.get_prop_choices()

	name = models.CharField('Characteristic', choices=choices, max_length=32)
	categories = models.ManyToManyField(Category)
	property_gr = models.CharField('Choice option (gr)', max_length=64, blank=True)
	property_en = models.CharField('Choice option (en)', max_length=64)

	def __str__(self):
		lst = list(map(lambda ctg: str(ctg), self.categories.all()))
		s = ', '.join(lst)
		return f'Choice option for "{ct.get_prop_trans(self.name)}" in categor{"y" if len(lst) == 1 else "ies"} "{s}": "{self.property_en}"'

	def save(self, *args, **kwargs):
		self.property_gr, self.property_en = save_langs(self.property_gr, self.property_en)
		super().save(*args, **kwargs)
		for category in ct.get_categories(self.name):
			self.categories.add(Category.objects.get(name=category))
		super().save(*args, **kwargs)

	class Meta:
		verbose_name = 'choice'
		verbose_name_plural = 'choices'