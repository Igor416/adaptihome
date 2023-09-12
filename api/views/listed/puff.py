from api import models
from .product import ProductView

class PuffView(ProductView):
  model = models.Puff