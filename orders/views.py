from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Customer

# Create your views here.

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