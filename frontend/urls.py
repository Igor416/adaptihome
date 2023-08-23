from django.urls import path
from .views import index

urlpatterns = [
	path('', index),
	path('shop/<str:category>/', index),
	path('product/<str:category>/<str:name>/', index),
	path('cart/', index),
	path('about/', index),
	path('contacts/', index),
]
