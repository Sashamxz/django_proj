from django.contrib import admin
from .models import Customer, Product, Order, Category


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
