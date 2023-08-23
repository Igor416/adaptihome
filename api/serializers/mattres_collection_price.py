from . import models, ModelSerializer

class MattressColectionsPriceSerializer(ModelSerializer):
  class Meta:
    fields = '__all__'
    model = models.Choice

  def to_representation(self, obj):
    size = None
    for m in models.Mattress.objects.filter(collection=obj):
      if size is None:
        size = m.sizes.first()
      elif not m.sizes.first() is None:
        if size.price > m.sizes.first().price:
          size = m.sizes.first()

    return {
      obj.property_gr: size.price
    }