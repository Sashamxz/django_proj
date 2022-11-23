from rest_framework import serializers
from crm.models import Order, Product
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('_all_')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('_all_')