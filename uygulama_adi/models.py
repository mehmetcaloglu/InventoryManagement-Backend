from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance) # Eğer UserProfile yoksa oluştur.

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Depot(models.Model):
    TYPE_CHOICES = (
        ('AnaDepo', 'Ana Depo'),
        ('AraDepo', 'Ara Depo'),
        ('MağazaDepo', 'Mağaza Depo'),
    )
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    depot = models.ForeignKey(Depot, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    min_required = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.depot.name}"

class Order(models.Model):
    STATUS_CHOICES = (
        ('Hazırlanıyor', 'Hazırlanıyor'),
        ('SevkEdildi', 'Sevk Edildi'),
        ('TeslimEdildi', 'Teslim Edildi'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class Sale(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale {self.id} for Order {self.order.id}"

class SupplierOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    expected_delivery = models.DateTimeField()

    def __str__(self):
        return f"Supplier Order {self.id} for {self.product.name}"
