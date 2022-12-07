
from django.contrib.auth import login, authenticate
from rest_framework import  generics, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission, SAFE_METHODS, IsAdminUser, \
    DjangoObjectPermissions
from crm.serializers import  RegisterSerializer




class RegisterUserView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        # Ensure that passwords match
        if request.data.get("password") != request.data.get("confirmation"):
            raise serializers.ValidationError({
                "password": "Passwords don't match"
            })
        response = super().create(request, *args, **kwargs)
        user = authenticate(request, username=request.data.get("username"), password=request.data.get("password"))
        if user is not None:
            login(request, user)
            return response
        raise serializers.ValidationError({
            "error": "cannot register"
        })
