from rest_framework import viewsets
from .models import Cliente
from .serializer import ClienteSerializer

class ClienteViewSets (viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
