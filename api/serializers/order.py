from api import models
from .lang_detective import LangDetectiveSerializer
from .size import SizeSerializer
from .listed import getListedProductsSerializer

class OrderSerializer(LangDetectiveSerializer):
  sizes = SizeSerializer(many=True)
  
  class Meta:
    exclude = ['id']
    model = models.Order
    
  def create(self, validated_data):
    order = models.Order.objects.create()
    return self.save_sizes(order, validated_data.pop('sizes'))
  
  def update(self, order, validated_data):
    order = self.save_sizes(order, validated_data.pop('sizes'))
    return super().update(order, validated_data)
  
  def save_sizes(self, order, sizes):
    existing = models.OrderedSize.objects.filter(order=order)
    created = []
    for raw_size in sizes:
      size = models.Size.objects.get(product=raw_size['product'], price=raw_size['price'])
      ordered_size = existing.filter(size=size)
      if ordered_size.exists():
        ordered_size.update(quantity=raw_size['quantity'])
        existing.difference(ordered_size)
      else:
        created.append((size, raw_size['quantity']))
    existing.delete()
    for size, quantity in created:
      models.OrderedSize.objects.create(order=order, size=size, quantity=quantity)
    order.save()
    return order
  
  def to_representation(self, instance):
    r = super().to_representation(instance)
    r['id'] = str(instance.id)
    sizes = r.pop('sizes')
    r['products'] = []
    for ordered_size, serialized_size in zip(models.OrderedSize.objects.filter(order=instance), sizes):
      model = getattr(models, ordered_size.size.category.name)
      product = model.objects.get(name=ordered_size.size.product)
      data = getListedProductsSerializer(model, self.lang).create(product, lang=self.lang).data
      serialized_size.update({'quantity': ordered_size.quantity})
      data['sizes'] = [serialized_size]
      r['products'].append(data)
    return r