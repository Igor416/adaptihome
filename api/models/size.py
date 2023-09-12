from django.db import models
from .category import Category

class Size(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Category')
    product = models.CharField('Product Name', max_length=32, blank=True)
    width = models.SmallIntegerField('Width', default=80)
    length = models.SmallIntegerField('Length', default=200)
    price = models.SmallIntegerField('Price (euro)', default=0)
    discount = models.SmallIntegerField('Discount (%)', default=0)
    
    @property
    def quantity(self):
        return 1

    def set_product_and_category(self, product, category):
        self.product = product
        self.category = category
        self.save()

    def __str__(self):
        return f'Size of {self.product}: {self.width} x {self.length} for {self.price} (EUR){f", with discount {self.discount}%" if self.discount != 0 else ""}'

    class Meta:
        verbose_name = 'size'
        verbose_name_plural = 'sizes'
        ordering = [models.F('price') * (100 - models.F('discount') / 100)]