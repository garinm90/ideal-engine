from django.db import models
from django.urls import reverse

# Create your models here.


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phone_number = models.CharField(max_length=10)
    customer_email = models.EmailField()
    customer_business_name = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return reverse('customer_detail', args=[str(self.id)])
    
class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    customer_number = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
