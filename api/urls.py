from django.urls import path
from .views import OrdersListView, OrdersCreateView

urlpatterns = [
    path('orders/', OrdersListView.as_view(), name='orders-list'),
    path('orders/create/', OrdersCreateView.as_view(), name='orders-create'),
]
