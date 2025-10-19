from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
import pyotp

from .models import Producto
from .serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


def home(request):
    return HttpResponse("¡Django está funcionando desde /api/!")


@api_view(['DELETE'])
def eliminar_producto(request, pk):
    codigo = request.data.get('codigo')
    
    # Secret global para todos los productos - usar variable de entorno en producción
    from django.conf import settings
    GLOBAL_2FA_SECRET = getattr(settings, 'GLOBAL_2FA_SECRET', "NMFUR4NR43HQH6Z4X754PHD6CG7BJC4D")
    
    try:
        producto = Producto.objects.get(pk=pk)
        totp = pyotp.TOTP(GLOBAL_2FA_SECRET)  # Usar secret global
        if not totp.verify(codigo):
            return Response({'detail': 'Código TOTP inválido'}, status=status.HTTP_401_UNAUTHORIZED)
        producto.delete()
        return Response({'detail': 'Producto eliminado'}, status=status.HTTP_204_NO_CONTENT)
    except Producto.DoesNotExist:
        return Response({'detail': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)