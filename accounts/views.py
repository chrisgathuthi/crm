import json

from django.shortcuts import render, HttpResponse
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import status
from django.views import View
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from .serializers import ClientSerializer, FieldWorkSerializer, BandwidthSerializer, ShortMessageSerializer, ProviderSerializer, UserSerializer, TokenSerializer, ProviderSerializer, ShortMessageSerializer, MpesaTransactionSerializer
from .models import Client, FieldWork, Bandwidth, ShortMessage, get_user_model, Provider, ShortMessage, MpesaTransaction
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .utilities import save_mpesa_results, get_provider_from_token
# Create your views here.


class ClientView(ModelViewSet):
    """client endpoint view class"""

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def perform_create(self, serializer):
        provider = get_provider_from_token(header=self.request.META)
        serializer.save(provider = provider )


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

    authentication_classes = [TokenAuthentication]

    def create(self, request):
        
        provider = get_provider_from_token(header=request.META)
        serialzer = ShortMessageSerializer(data=request.data)
        if serialzer.is_valid(raise_exception=True):
            serialzer.save(provider = provider)
            return Response(data=serialzer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request):

        provider = get_provider_from_token(header=request.META)
        queryset = ShortMessage.objects.filter(provider=provider).order_by("-timestamp")
        serializer = ShortMessageSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
  
class UserView(ViewSet):

    """creating partner instance view"""
    
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            token = Token.objects.filter(user__email=serializer.validated_data["email"]).first()
            return Response(data={"token": str(token)}, status=status.HTTP_201_CREATED)

class ProviderView(ViewSet):

    """provider view"""

    def create(self, request):
        """create provider profile"""
        user_token = request.META.get("HTTP_AUTHORIZATION").split()[1]        
        
        try:
            user = Token.objects.get(key=user_token)
        except Exception as e:
            return Response(data={"message":"No token found proceed to login"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = ProviderSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(owner = user.user)
                return Response(data={"provider":"provider created successfully"}, status=status.HTTP_201_CREATED)

class MpesaTransactions(ViewSet):

    """mpesa transaction endpoint view"""

    authentication_classes = [TokenAuthentication]
    
    queryset = MpesaTransaction.objects.all()

    def list(self, request):
        serilizer = MpesaTransactionSerializer(self.queryset, many=True)
        return Response(data=serilizer.data, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name="dispatch")
class MpesaWebHook(View):

    """mpesa callback"""

    def post(self, request):
        save_mpesa_results(results=json.loads(request.body))
        return JsonResponse(data={"ResultCode":"0", "ResultDesc":"Success"})


    
