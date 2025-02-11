from django.shortcuts import render

from rest_framework import viewsets
from.models import Clientes
from .serializers import ClientesSerializer
from rest_framework.permissions import AllowAny

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    permission_classes = [AllowAny]

#IsAuthenticated para formularios 