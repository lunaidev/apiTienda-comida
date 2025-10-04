from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Producto

from .serializers import ProductoSerializer




class ProductoViewSet(viewsets.ModelViewSet):

    queryset = Producto.objects.all()

    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
        })