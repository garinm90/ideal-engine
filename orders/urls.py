from django.urls import path

from . import views

urlpatterns = [
    path('', views.CustomerListView.as_view(), name='home'),
    path('customer/new/', views.CustomerCreateView.as_view(), name='customer_new'),
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('customer/<int:pk>/delete', views.CustomerDeleteView.as_view(), name='customer_delete'),
    path('customer/<int:pk>/edit', views.CustomerUpdateView.as_view(), name='customer_edit'),
    path('customer/<int:pk>/orders', views.CustomerOrdersView.as_view(), name='customer_orders'),
    path('order/', views.OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('order/<int:pk>/edit', views.OrderUpdateView.as_view(), name='order_edit'),
    path('order/new', views.OrderCreateView.as_view(), name='order_new'),
    path('ride/new', views.RideCreateView.as_view(), name='ride_new'),
    path('controller/new', views.create_controller, name='controller_new'),
    path('controller/<int:pk>/', views.ControllerDetailView.as_view(), name='controller_detail'),
    path('controller/image', views.image_upload, name='upload_image'),
    path('controller/', views.ControllerListView.as_view(), name='controller_list')
]

