# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.db.models.signals import post_save


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
#     role = models.CharField(max_length=50, default='staff_manager')  # varsayılan değer olarak 'User' kullanılıyor
#     depotname = models.ForeignKey('Depot', on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return self.user.username
 
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import UserProfile


# # @receiver(post_save, sender=User)
# # def create_or_update_user_profile(sender, instance, created, **kwargs):
# #     if created:
# #         UserProfile.objects.get_or_create(user=instance)

# class Category(models.Model):
#     name = models.CharField(max_length=255, unique=True)

#     def __str__(self):
#         return self.name

# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class Depot(models.Model):
#     TYPE_CHOICES = (
#         ('AnaDepo', 'Ana Depo'),
#         ('AraDepo', 'Ara Depo'),
#         ('MağazaDepo', 'Mağaza Depo'),
#     )
#     name = models.CharField(max_length=255)
#     type = models.CharField(max_length=30, choices=TYPE_CHOICES)
#     location = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class Stock(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     depot = models.ForeignKey(Depot, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     min_required = models.PositiveIntegerField()

#     def __str__(self):
#         return f"{self.product.name} - {self.depot.name}"

# class Order(models.Model):
#     STATUS_CHOICES = (
#         ('Hazırlanıyor', 'Hazırlanıyor'),
#         ('SevkEdildi', 'Sevk Edildi'),
#         ('TeslimEdildi', 'Teslim Edildi'),
#     )
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     order_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=30, choices=STATUS_CHOICES)

#     def __str__(self):
#         return f"Order {self.id} by {self.user.username}"

# class Sale(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     sale_date = models.DateTimeField(auto_now_add=True)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Sale {self.id} for Order {self.order.id}"
    
# class Supplier (models.Model):
#     name = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)
#     def __str__(self):
#         return self.name

# class SupplierOrder(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     order_date = models.DateTimeField(auto_now_add=True)
#     expected_delivery = models.DateTimeField()

#     def __str__(self):
#         return f"Supplier Order {self.id} for {self.product.name}"
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    role = models.CharField(max_length=50, default='staff_manager')
    depotname = models.ForeignKey('Depot', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username

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
    source_depot = models.ForeignKey(Depot, on_delete=models.CASCADE, related_name='order_source', null=True, blank=True)
    destination_depot = models.ForeignKey(Depot, on_delete=models.CASCADE, related_name='order_destination',null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Order {self.id} from {self.depot.name}"

class Sale(models.Model):
    store = models.ForeignKey(Depot, on_delete=models.CASCADE, limit_choices_to={'type': 'MağazaDepo'})
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale {self.id} at {self.store.name}"

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SupplierOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    expected_delivery = models.DateTimeField()

    def __str__(self):
        return f"Supplier Order {self.id} for {self.product.name}"

class Transaction(models.Model):
    source_depot = models.ForeignKey(Depot, related_name='source_transactions', on_delete=models.CASCADE)
    destination_depot = models.ForeignKey(Depot, related_name='destination_transactions', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} from {self.source_depot.name} to {self.destination_depot.name}"
