
from django.urls import path
from django.conf.urls import include
from . import views



urlpatterns = [
   path('auth/', include('rest_framework.urls')),
   path('register', views.RegisterUserView.as_view(), name="register"),
 ]
