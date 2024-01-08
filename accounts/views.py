import json

from django.contrib.auth import get_user_model
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.shortcuts import HttpResponse, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from .models import (Bandwidth, Client, FieldWork, MpesaTransaction, Provider,
                     ShortMessage, get_user_model)
from .serializers import (BandwidthSerializer, ClientSerializer,
                          FieldWorkSerializer, MpesaTransactionSerializer,
                          ProviderSerializer, ShortMessageSerializer,
                          TokenSerializer, UserSerializer, AuthenticationSerializer)
from .utilities import get_provider_from_token, save_mpesa_results

# Create your views here.


class ClientView(ModelViewSet):
    """client endpoint view class"""

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        provider = get_provider_from_token(header=self.request.META)
        serializer.save(provider=provider)


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
            serialzer.save(provider=provider)
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
            token = Token.objects.filter(
                user__email=serializer.validated_data["email"]
            ).first()
            return Response(data={"token": str(token)}, status=status.HTTP_201_CREATED)
import pprint
class UserAuthenticateView(ViewSet):

    def create(self, request):
        serializer = AuthenticationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(username=serializer.data["username"], password=serializer.data["password"])
            if user is not None:
                token = Token.objects.get(user=user)
                return Response(data={"token":token}, status=status.HTTP_200_OK)
            return Response(data={"password":"invalid credential","username":"invalid username"}, status=status.HTTP_400_BAD_REQUEST)
            
class ProviderView(ViewSet):

    """provider view"""

    def create(self, request):
        """create provider profile"""
        user_token = request.META.get("HTTP_AUTHORIZATION").split()[1]

        try:
            user = Token.objects.get(key=user_token)
        except Exception as e:
            return Response(
                data={"message": "No token found proceed to login"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        else:
            serializer = ProviderSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(owner=user.user)
                return Response(
                    data={"provider": "provider created successfully"},
                    status=status.HTTP_201_CREATED,
                )

    def retrieve(self, request):
        """get provider year joined"""
        provider = get_provider_from_token(header=request.META)
        provider_instance = Provider.objects.get(id=provider.id)
        serializer = ProviderSerializer(provider_instance)
        return Response(data={"yearJoined": serializer.data["join_date"]})


class MpesaTransactions(ViewSet):

    """mpesa transaction endpoint view"""

    authentication_classes = [TokenAuthentication]

    def list(self, request):
        provider = get_provider_from_token(request.META)
        queryset = MpesaTransaction.objects.filter(
            provider__serial_number=provider.serial_number
        )
        serilizer = MpesaTransactionSerializer(queryset, many=True)
        return Response(data=serilizer.data, status=status.HTTP_200_OK)

    def retrieve(self, request):
        """filtering mpesa transactions using client serial"""

        if request.query_params is not None:
            queryset = MpesaTransaction.objects.filter(
                client__serial=request.query_params.get("search")
            )
            serializer = MpesaTransactionSerializer(queryset, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            queryset = MpesaTransaction.objects.none()
            serializer = MpesaTransactionSerializer(queryset, many=True)
            return Response(data=serializer.data, status=status.HTTP_404_NOT_FOUND)


@method_decorator(csrf_exempt, name="dispatch")
class MpesaWebHook(View):

    """mpesa callback"""

    def post(self, request):
        save_mpesa_results(results=json.loads(request.body))
        return JsonResponse(data={"ResultCode": "0", "ResultDesc": "Success"})
