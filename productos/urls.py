from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ProductoViewSet, eliminar_producto


router = DefaultRouter()

router.register(r'productos', ProductoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('productos/<int:pk>/eliminar/', eliminar_producto, name='eliminar_producto'),  # Eliminar con TOTP
]