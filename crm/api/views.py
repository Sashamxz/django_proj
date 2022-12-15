from django.shortcuts import render
from django.contrib.auth import login, authenticate
from rest_framework import status, generics, serializers
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission, SAFE_METHODS, IsAdminUser, \
    DjangoObjectPermissions
from .serializers import ProductSerializer, UserSerializer, CustomerSerializer
from crm.models import Product, Customer



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getRoutes(request):
    routes = [
        '/api/users/',
        '/api/products/',
        '/api/customers/',
    ]
    return Response(routes)





class LoginUserView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        user = authenticate(request, username=request.data.get("username"), password=request.data.get("password"))
        if user is not None:
            login(request, user)
            return Response("Successful login")
        raise serializers.ValidationError({
            "error": "cannot login"
        })



class UsersListView(APIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        if users:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



class ProductsListView(APIView):       
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



class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




class CustomersListView(APIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


    def get(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        if customers:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)