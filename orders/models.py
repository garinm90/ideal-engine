from django.db import models
from django.urls import reverse

# Create your models here.


class Customer(models.Model):
    customer_first_name = models.CharField(max_length=100)
    customer_last_name = models.CharField(max_length=100, null=True)
    customer_phone_number = models.CharField(max_length=10)
    customer_email = models.EmailField()
    customer_business_name = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_first_name

    def get_absolute_url(self):
        return reverse('customer_detail', args=[str(self.id)])
    
class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    customer_number = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.order_number)

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.order_number)])
