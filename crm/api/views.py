from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import OrderSerializer, CustomerSerializer, ProductSerializer, CategorySerializer


from crm.models import Product, Customer, Order, Category


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getRoutes(request):
    routes = [
        '/api/users/',
        '/api/products/',
        '/api/customers/',
        '/api/orders/',
        '/api/cutegories/'
    ]
    return Response(routes)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class OrederViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class CategoryesApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)


# class ProductsListView(generics.ListCreateAPIView):
#     serializer_class = ProductSerializer
#     permission_classes = (AllowAny,)
#     queryset = Product.objects.all()

#     def get(self, request, *args, **kwargs):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         if products:
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def post(self, request, *args, **kwargs):
#         '''
#         Create the Product
#         '''
#         data = {
#             'name': request.data.get('name'),
#             'price': request.data.get('price'),
#             'category': request.data.get('category'),
#             'description' : request.data.get('description')
#         }
#         serializer = ProductSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProductDetailView(APIView):
#     permission_classes = (IsAdminUser)
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class CustomersListView(APIView):
#     serializer_class = CustomerSerializer
#     queryset = Customer.objects.all()

#     def get(self, request, *args, **kwargs):
#         customers = Customer.objects.all()
#         serializer = CustomerSerializer(customers, many=True)
#         if customers:
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)
