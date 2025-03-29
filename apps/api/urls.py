from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.usuarios.views import UserViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),

]


