from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import CrmHome,  LoginUser,  RegisterUser, AddProduct,  about, logout_user

urlpatterns = [
    path('', CrmHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addproduct/', AddProduct.as_view(), name='add_product'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),

]