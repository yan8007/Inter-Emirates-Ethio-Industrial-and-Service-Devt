from django.urls import path
from . import views

urlpatterns = [
    path('warehouses/', views.WarehouseListView.as_view(), name='warehouse-list'),
    path('stock-items/', views.StockItemListView.as_view(), name='stock-item-list'),
]
