import uuid
from . import models, Size

class Order(models.Model):
  id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
  sizes = models.ManyToManyField(Size, through='OrderedSize', through_fields=('order', 'size'), verbose_name='Picked Sizes', blank=True)
  total = models.IntegerField('Total', default=0)
  email = models.EmailField('Email', blank=True)
  city = models.CharField('City', max_length=32, blank=True, default='Lemasos')
  phone = models.CharField('Phone', max_length=16, blank=True)
  address = models.CharField('Address', max_length=128, blank=True)
  shipping = models.CharField('Shipping Method', choices=(('showroom', 'showroom'), ('courier', 'courier')), max_length=8, default='showroom')
  
  def __str__(self):
    return f'Order #' + str(self.id)
  
  class Meta:
    verbose_name = 'Order'
    verbose_name_plural = 'Orders'

class OrderedSize(models.Model):
  order = models.ForeignKey(Order, verbose_name='Order', on_delete=models.CASCADE)
  size = models.ForeignKey(Size, verbose_name='Size', on_delete=models.CASCADE)
  quantity = models.SmallIntegerField('Quantity', default=1)
  
  def __str__(self):
    return f'{self.size} x{self.quantity} in order {self.order}'
