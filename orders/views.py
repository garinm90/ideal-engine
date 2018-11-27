from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from orders.models import Customer, Order, Ride, Controller
from orders.forms import ControllerForm, ControllerImageForm

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

class OrderUpdateView(UpdateView):
    model = Order
    fields = '__all__'
    template_name = 'order_edit.html'

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

class RideListView(ListView):
    model = Ride
    template_name = 'ride_list.html'

class ControllerDetailView(DetailView):
    model = Controller
    template_name = 'controller_detail.html'

class ControllerListView(ListView):
    model = Controller
    template_name = 'controller_list.html'

def create_controller(request):
    if request.method == 'POST':
        form = ControllerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = ControllerForm()
    
    context = {
        'form': form,
    }
    return render(request, 'controller_new.html', context)

def image_upload(request):
    if request.method == 'POST':
        form = ControllerImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
        else:
            print(form.erros)
    else:
        form = ControllerImageForm()
    return render (request, 'upload_image.html', {'form':form})