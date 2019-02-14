from django.db import models
# from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser
from datetime import datetime 
# from django.
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
	prod_name = models.CharField(max_length=250)
	prod_price = models.DecimalField(max_digits=9, decimal_places=2)
	is_available = models.BooleanField(default=True)
	quantity = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return self.prod_name + ' - Rs.' + str(self.prod_price)
'''
class ProfileUser(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=250)
	mobile = models.CharField(max_length=10, null=True, blank=True)
	# password = models.CharField(max_length=250)
	USERNAME_FIELD = 'email'

	objects = UserManager()

	def __str__(self):
		return self.name
'''

class ProfileUser(AbstractUser):
	name = models.CharField(max_length=250)
	mobile = models.CharField(max_length=10, null=True, blank=True)
	email = models.CharField(max_length=100)
	is_vendor = models.BooleanField(default=False)
	# product_purchased = models.

	def __str__(self):
		return self.name

class Order(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
	price = models.PositiveIntegerField(default=0)
	quantity = models.PositiveSmallIntegerField(default=1)
	final_price = models.PositiveIntegerField(default=0)
	order_date = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
	user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
	products = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	total_price = models.PositiveIntegerField(default=0)

'''
class VendorUser(AbstractUser):
	vendor_name = models.CharField(max_length=250)
	vendor_mobile = models.CharField(max_length=10, null=True, blank=True)
	vendor_email = models.CharField(max_length=100)
	# products = models.ForeignKey(Product, )

	def __str__(self):
		return self.name
'''

class VendorAndProduct(models.Model):
	# product = models.ForeignKey(Product, on_delete=models.CASCADE)
	# vendor_id = models.ForeignKey(VendorUser, on_delete=models.CASCADE)
	product_name = models.CharField(max_length=50)
	product_colour = models.CharField(max_length=50)
	product_screen_size = models.CharField(max_length=10)
	product_os = models.CharField(max_length=50)
	product_ram = models.CharField(max_length=10)
	product_memory = models.CharField(max_length=10)
	product_price = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.product_name

