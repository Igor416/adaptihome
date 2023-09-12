from api import models
from .product import ProductView

class TableView(ProductView):
  model = models.Table