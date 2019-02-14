from django.contrib import admin

from .models import Product, ProfileUser, Order, Cart, VendorAndProduct
# Register your models here.
admin.site.register(Product)
admin.site.register(ProfileUser)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(VendorAndProduct)