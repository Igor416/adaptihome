from django.contrib import admin
from . import models
from . import catalog as ct
from .forms import ProductForm

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ['id']

@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_filter = ('categories',)
    ordering = ['name']
    exclude = ['categories']

@admin.register(models.Technology)
class TechnologAdmin(admin.ModelAdmin):
    ordering = ['name_en']

@admin.register(models.Size)
class SizeAdmin(admin.ModelAdmin):
    list_filter = ('category', 'product', 'discount')
    exclude = ['category', 'product']
    ordering = ['category', 'product', 'length', 'price']

class ImageListFilter(admin.SimpleListFilter):
    title = ('categories')
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        return [(product_name, ct.get_pr_trans(product_name)) for product_name in ct.get_all_categories()]

    def queryset(self, request, queryset):
        if self.value():
            resp = queryset.none()
            for entry in getattr(models, self.value()).objects.all():
                resp |= queryset.filter(image__startswith='products/' + entry.name)

            return resp

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_filter = (ImageListFilter, )

class LayerMattressInline(admin.TabularInline):
    model = models.LayerMattress
    extra = 3

class LayerPillowInline(admin.TabularInline):
    model = models.LayerPillow
    extra = 3

class LayerMattressPadInline(admin.TabularInline):
    model = models.LayerMattressPad
    extra = 3

@admin.action(description='Remove discount')
def remove_discount(modeladmin, request, queryset):
    queryset.update(discount=0)

for product_name in ct.get_all_categories():
    form = type(product_name + 'Form', (ProductForm,), {})
    model = getattr(models, product_name)
    model._meta.verbose_name, model._meta.verbose_name_plural = ct.get_pr_trans(product_name), ct.get_pr_trans(product_name, plural=True)
    setattr(form, 'model', model)
        
    layers = {
        ct.MATTRESS: LayerMattressInline,
        ct.PILLOW: LayerPillowInline,
        ct.MATTRESSPAD: LayerMattressPadInline
    }

    attrs = {
        'form': form,
        'actions': (remove_discount,)
    }
    
    if product_name in layers.keys():
        attrs.update({'inlines': (layers[product_name],)})

    admin_model = type(product_name + 'Admin', (admin.ModelAdmin,), attrs)
    admin.site.register(model, admin_model)

class OrderedSizeInline(admin.TabularInline):
    model = models.OrderedSize
    extra = 1

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderedSizeInline,)