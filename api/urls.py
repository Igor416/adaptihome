from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.SearchView.as_view()),
    path('mattress_category_prices/', views.MattressColectionsPriceView.as_view()),
    path('products/folding_bed/', views.FoldingBedView.as_view()),
    path('products/bed/', views.BedView.as_view()),
    path('products/mattress/', views.MattressView.as_view()),
    path('products/table/', views.TableView.as_view()),
    path('products/accessories/', views.AccessoriesView.as_view()),
    path('products/puff/', views.PuffView.as_view()),
    path('product/<str:category>/<str:name>/', views.ProductView.as_view()),
    path('order/<str:id>/', views.OrderView.as_view())
]
