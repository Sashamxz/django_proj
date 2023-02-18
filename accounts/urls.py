from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .api import LoginUserView, RegisterApi, LogoutAndBlacklistRefreshTokenForUserView, UsersListView


urlpatterns = [
    path('user/create/', RegisterApi.as_view(), name='create_user'),
    path('token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login', LoginUserView.as_view(), name="login"),
    path('logout', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name="logout"),
    path('users/', UsersListView.as_view(), name='users'),
]
