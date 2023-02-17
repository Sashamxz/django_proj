from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(default='ekta dd.jpg', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    STATUS = [
        ('Pending' , 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    ]
    URGENCY_CHOICES = [
        ('1', 'not urgent'),
        ('2', 'several days'),
        ('3', 'about a 1-2 week'),
        ('4', 'urgently'),
    ]

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)
    urgency = models.CharField(max_length=1, choices=URGENCY_CHOICES, default='1',)

    def __str__(self):
        return self.product.name
