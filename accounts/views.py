import json

from django.shortcuts import render, HttpResponse
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import status
from .serializers import ClientSerializer, FieldWorkSerializer, BandwidthSerializer, ShortMessageSerializer, ProviderSerializer, UserSerializer, TokenSerializer
from .models import Client, FieldWork, Bandwidth, ShortMessage, get_user_model

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

class ShortMessageView(ViewSet):

    """short message view"""
    queryset = ShortMessage.objects.all()

    def create(self, request):
        serialzer = ShortMessageSerializer(data=request.data)
        if serialzer.is_valid(raise_exception=True):
            serialzer.save()
            return Response(data=serialzer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        serializer = ShortMessageSerializer(self.queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
  
class UserView(ViewSet):

    """creating partner instance view"""
    
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            token = Token.objects.filter(user__email=serializer.validated_data["email"]).first()
            return Response(data={"token": str(token)}, status=status.HTTP_201_CREATED)
    