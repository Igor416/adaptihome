from api import models
from .product import ProductView

class BedView(ProductView):
  model = models.Bed