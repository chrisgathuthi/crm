from django.shortcuts import render, HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import ClientSerializer, FieldWorkSerializer, BandwidthSerializer
from .models import Client, FieldWork, Bandwidth

# Create your views here.


class ClientView(ModelViewSet):
    """client endpoint view class"""

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class FieldWorkView(ModelViewSet):
    """field word view class"""

    queryset = FieldWork.objects.all()
    serializer_class = FieldWorkSerializer


class BandwidthView(ModelViewSet):
    """Band word view class"""

    queryset = Bandwidth.objects.all()
    serializer_class = BandwidthSerializer
