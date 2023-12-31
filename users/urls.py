from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserViewSet, MyObtainPairView

app_name = UsersConfig.name

rout = DefaultRouter()
rout.register('users', UserViewSet, basename='user')


urlpatterns = [
    path('token/', MyObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + rout.urls
