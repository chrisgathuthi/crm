from django.shortcuts import render, HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import ClientSerializer, FieldWorkSerializer
from .models import Client, FieldWork
# Create your views here.

class ClientView(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class FieldWorkView(ModelViewSet):
    queryset = FieldWork.objects.all()
    serializer_class = FieldWorkSerializer