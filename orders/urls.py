from django.urls import path

from . import views

urlpatterns = [
    path('', views.CustomerListView.as_view(), name='home'),
    path('customer/new/', views.CustomerCreateView.as_view(), name='customer_new'),
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('customer/<int:pk>/delete', views.CustomerDeleteView.as_view(), name='customer_delete'),
    path('customer/<int:pk>/edit', views.CustomerUpdateView.as_view(), name='customer_edit'),
    path('order/', views.OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('order/new', views.OrderCreateView.as_view(), name='order_new'),
]