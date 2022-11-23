from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ProductViewSet, UserViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('product', ProductViewSet)



urlpatterns = [
    path('', include(router.urls)),
]