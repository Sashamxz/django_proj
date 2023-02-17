from rest_framework import serializers
from crm.models import Order, Product, Customer, Category


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'status']

    def create(self, validated_data):
        order = Order.objects.create_orfer(**validated_data)
        return order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('pk', 'name', 'phone', 'email', 'description')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fieleds = ('pk', 'name')