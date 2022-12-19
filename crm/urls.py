from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import CrmHome,  LoginUser,  RegisterUser, AddProduct, CustomerDetail, AddCustomer, \
        AddOrder, ShowCustomers, ShowProducts, ProductDetail, ShowOrders, OrderDetail, about, logout_user



urlpatterns = [
    #auth    
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    #common
    path('', CrmHome.as_view(), name='home'),
    path('about/', about, name='about'),
    #crm  
    
    # product   
    path('add-product/', AddProduct.as_view(), name='add-product'),
    path('show-products/', ShowProducts.as_view(), name='show-products'),
    path('product-detail/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    
    #customer
    path('customers/', ShowCustomers.as_view(), name='shoe-customers'),
    path('create-customer/', AddCustomer.as_view(), name='create-customer') ,
    path('customer/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),
    
    #order
    path('orders/', ShowOrders.as_view(), name='show-orders'),
    path('add-order/', AddOrder.as_view(), name='add-order'),
    path('order//<int:pk>/', OrderDetail.as_view(), name='order-deatil'),
    path('update-order/<int:pk>/', about, name="update-order"),
    path('delete-order/<int:pk>/', about, name="delete-order")
]