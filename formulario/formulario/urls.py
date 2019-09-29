from django.contrib import admin
from django.urls import path, include
from core.api.viewsets import ClienteViewSet
from rest_framework import routers
from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register(r'Clientes', ClienteViewSet, base_name='name')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
]
