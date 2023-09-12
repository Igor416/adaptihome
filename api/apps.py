from django.apps import AppConfig

class ApiConfig(AppConfig):
    name = 'api'
    verbose_name = 'Work Space'
    
    def ready(self):
        from . import models, catalog as ct

        for product_name in ct.get_all_categories():
            model = getattr(models, product_name)
            model.set_manager()
        
