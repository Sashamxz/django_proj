from rest_framework import serializers
from crm.models import Order, Product, Customer, Category


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    urgency = serializers.StringRelatedField()
    class Meta:
        model = Order
        fields = ['id', 'customer', 'product', 'status', 'urgency', 'date_created']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'description']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'phone', 'email', 'description')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fieleds = ('id', 'name')