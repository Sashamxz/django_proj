from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, OreserViewSet, CategoryesApiView, CustomerViewSet, getRoutes

router = routers.DefaultRouter()

router.register(r'customers', CustomerViewSet)
router.register(r'orders', OreserViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('', getRoutes),
    path('categoryes/' , CategoryesApiView.as_view()),
    path('v1/', include((router.urls, 'crm'))),
]
