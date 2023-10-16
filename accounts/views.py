from django.shortcuts import render, HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import ClientSerializer
from .models import Client
# Create your views here.

class ClientView(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


