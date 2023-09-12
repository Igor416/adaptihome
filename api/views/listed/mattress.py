from api import models
from .product import ProductView

class MattressView(ProductView):
  model = models.Mattress