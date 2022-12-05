from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ProductSerializer, UserSerializer, CustomerSerializer
from crm.models import Product, Customer



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getRoutes(request):
    routes = [
        '/api/users/',
        '/api/products/',
        '/api/token/customers/',
    ]
    return Response(routes)




class UserView(APIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        if users:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



class ProductView(APIView):       
    serializer_class = ProductSerializer         
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        if products:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



    def post(self, request, *args, **kwargs):
        '''
        Create the Product with given todo data
        '''
        data = {
            'name': request.data.get('name'), 
            'price': request.data.get('price'), 
            'category': request.data.get('category'),
            'description' : request.data.get('description')
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CustomerView(APIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


    def get(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        if customers:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)