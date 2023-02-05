from django.urls import path
from django.contrib.auth.views import LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views


urlpatterns = [
    path('', views.getRoutes),
    path('user/create/', views.RegisterApi.as_view(), name='create_user'),
    path('token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('blacklist/', views.LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),
    path('login', views.LoginUserView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('users/', views.UsersListView.as_view(), name='users'),
    path('products/', views.ProductsListView.as_view(), name='products'),
    path('customers/', views.CustomersListView.as_view(), name='customers')
    ]
