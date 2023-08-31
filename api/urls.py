from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.SearchView.as_view()),
    path('mattress_category_prices/', views.MattressColectionsPriceView.as_view()),
    path('products/<str:category>/', views.ListProductView.as_view()),
    path('products/<str:category>/<str:filter>/', views.ListProductView.as_view()),
    path('product/<str:category>/<str:name>/', views.RetrieveProductView.as_view()),
    path('order/<str:id>/', views.OrderView.as_view())
]
