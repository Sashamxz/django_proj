from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ProductSerializer, UserSerializer, CustomerSerializer
from crm.models import Product, Customer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)



class ProductViewSet(viewsets.ModelViewSet):       
    serializer_class = ProductSerializer         
    queryset = Product.objects.all()



class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
