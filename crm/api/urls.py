from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ProductViewSet, UserViewSet, CustomerViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('products', ProductViewSet)
router.register('customers', CustomerViewSet)



urlpatterns = [
    path('', include(router.urls)),
]