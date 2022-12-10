from django.urls import path, re_path
from django.contrib.auth.views import LogoutView, LoginView
from rest_framework import routers
from django.conf.urls import include

from . import views





urlpatterns = [
 
    path('', views.getRoutes),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('login', views.LoginUserView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('users/', views.UserView.as_view(), name='users'),
    path('products/', views.ProductView.as_view(), name='products'),
    path('customers/', views.CustomerView.as_view(), name='customers')
]