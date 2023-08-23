from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.SearchView.as_view()),
    path('mattress_category_prices/', views.MattressColectionsPriceView.as_view()),
    path('products/<str:category>/', views.ListedProductsView.as_view()),
    path('products/<str:category>/<str:filter>/', views.ListedProductsView.as_view()),
    path('product/<str:category>/<str:name>/', views.DetailedProductView.as_view()),
    path('worker/', views.WorkerView.as_view())
]
