from django.db import models
from django.urls import reverse, reverse_lazy

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

class Ride(models.Model):
    ride_name = models.CharField(max_length=100)

    def __str__(self):
        return self.ride_name

    def get_absolute_url(self):
        return reverse_lazy('home')


class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    customer_number = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    description = models.CharField(max_length=200, null=True)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='orders', null=True)

    def __str__(self):
        return str(self.order_number) + ' ' + str(self.customer_number) + ' ' + str(self.ride)

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.order_number)])


class Controller(models.Model):
    # controller_model_choices = (
    #     ('T8000', 'T8000'),
    #     ('T4000', 'T4000'),
    #     ('YM-ST4K', 'YM-ST4K'),
    #     ('YM-ST8K', 'YM-ST8K'),
    # )
    controller_number = models.IntegerField(unique=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='controller')
    # controller_model = models.CharField(max_length=100, choices=controller_model_choices, default='T8000')
    T8000 = models.IntegerField(null=True, blank=True)
    T4000 = models.IntegerField(null=True, blank=True)
    T1000 = models.IntegerField(null=True, blank=True)
    T1000s = models.IntegerField(null=True,blank=True)
    F16V3 = models.IntegerField(null=True, blank=True)
    F4V3 = models.IntegerField(null=True, blank=True)
    F2_Raspberry_Pi = models.IntegerField(null=True, blank=True)
    Raspberry_Pi = models.IntegerField(null=True, blank=True)

    Two_Forty_24_Volt = models.IntegerField(null=True, blank=True)
    Three_Twenty_24_Volt = models.IntegerField(null=True, blank=True)

    TP_Link = models.IntegerField(null=True, blank=True)

    Buck_Converter_24v_to_5v = models.IntegerField(null=True, blank=True)
    Buck_Converter_24v_to_12v = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.controller_number