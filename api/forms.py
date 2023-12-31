from django import forms
from . import models
from . import catalog as ct

class ProductForm(forms.ModelForm):
	class Meta:
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		images = models.Image.objects.all()
		image_name = self.instance.name.replace(' ', '_')

		for name, field in self.fields.items():
			if hasattr(field, 'queryset'):
				if name == 'category':
					field.initial = models.Category.objects.get(name=self.model.get_name())
					field.disabled = True

				elif name == 'sizes':
					category = models.Category.objects.get(name=self.model.get_name())
					by_category = models.Size.objects.filter(category=category, product=self.instance.name)
					field.queryset = by_category | models.Size.objects.filter(category=None, price__gt=0)

				elif name == 'shortcut':
					filtered = filter(lambda i: i.is_shortcut(), images)
					field.queryset = images.filter(pk__in=[item.pk for item in filtered], image__endswith=image_name + '.jpg')

				elif name == 'images':
					filtered = filter(lambda i: not i.is_shortcut(), images)
					field.queryset = images.filter(pk__in=[item.pk for item in filtered], image__contains=image_name + '_')

				elif name.startswith('rigidity'):
					field.label = ct.get_prop_trans(name[:-1]) + ' ' + name[-1]
					field.queryset = models.Choice.objects.filter(name=name[:-1])

				elif name == 'recomended':
					field.queryset = models.Choice.objects.filter(name='collection')

				elif name.startswith('suggestions'):
					model = getattr(models, name.split('_')[1])
					field.label = f'Suggestions ({model.get_name()}):'
					field.queryset = model.objects.all()

				elif not name.endswith('dimensions'):
					field.label = ct.get_prop_trans(name)
					field.queryset = models.Choice.objects.filter(name=name)

			else:
				try:
					field.label = ct.get_prop_trans(name)
				except:
					pass

		setattr(self.Meta, 'model', self.model)