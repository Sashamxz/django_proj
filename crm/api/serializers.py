from rest_framework import serializers
from crm.models import Order, Product, Customer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User







class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'status']

    def create(self, validated_data):
        order = Order.objects.create_orfer(**validated_data)
        Token.objects.create(order=order)
        return order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ 'name', 'price','category', 'description']




class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('pk', 'name','phone',  'email', 'description')
