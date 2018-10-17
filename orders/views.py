from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Customer, Order, Ride, Controller

# Create your views here.

class CustomerOrdersView(DetailView):
    model = Customer
    template_name = 'customer_orders.html'

class CustomerListView(ListView):
    model = Customer
    template_name = 'home.html'

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer_new.html'
    fields = '__all__'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_delete.html'
    success_url = reverse_lazy('home')
    
class CustomerUpdateView(UpdateView):
    model = Customer
    fields = '__all__'
    template_name = 'customer_edit.html'


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_new.html'
    fields = ['customer_number', 'ride', 'description']

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'

class RideCreateView(CreateView):
    model = Ride
    template_name = 'ride_new.html'
    fields = '__all__'

class ControllerCreateView(CreateView):
    model = Controller
    template_name = 'controller_new.html'
    fields = '__all__'