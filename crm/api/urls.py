from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ProductView, UserView, CustomerView
from . import views





urlpatterns = [
    path('', views.getRoutes),
    path('users/', UserView.as_view(), name='users'),
    path('products/', ProductView.as_view(), name='products'),
    path('customers/', CustomerView.as_view(), name='customers')
]