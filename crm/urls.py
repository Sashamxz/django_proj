from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import CrmHome,  LoginUser,  RegisterUser, AddProduct, CustomerDetail, CreateCustomer, \
              CreateOrder, about, logout_user, customer_list



urlpatterns = [
    #auth    
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    #common
    path('', CrmHome.as_view(), name='home'),
    path('about/', about, name='about'),
    #crm     
    path('add-product/', AddProduct.as_view(), name='add-product'),
    path('orders/', AddProduct.as_view(), name='orders'),
    path('customers/', customer_list, name='customers'),
    path('create-customer/', CreateCustomer.as_view(), name='create-customer') ,
    path('customer/<str:pk>/', CustomerDetail.as_view(), name='customer'),
    path('create-order/', CreateOrder.as_view(), name='create-order'),
    path('update-order/<str:pk>/', about, name="update-order"),
    path('delete-order/<str:pk>/', about, name="delete-order")
]