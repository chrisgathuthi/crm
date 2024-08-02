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
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import (Bandwidth, Client, FieldWork, MpesaTransaction, Provider,
                     ShortMessage, Employee, Material, SmsGatewayResponse, Inventory)
from .serializers import (BandwidthSerializer, ClientSerializer,
                          FieldWorkSerializer, MpesaTransactionSerializer,
                          ProviderSerializer, ShortMessageSerializer,
                          TokenSerializer, UserSerializer, AuthenticationSerializer, BandwidthSerializer,  MaterialSerializer, SmsGatewayResponseSerializer, EmployeeSerializer, InventorySerializer)
from .utilities import get_provider_from_token, save_mpesa_results,check_token_validation

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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['isclosed']


    def list(self, request):

        import json
        query_params = json.loads(request.query_params.get('isclosed'))

        provider = get_provider_from_token(header=self.request.META)
        queryset = FieldWork.objects.filter(provider=provider)
        queryset = queryset.filter(isclosed=query_params)
        serializer = FieldWorkSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        provider = get_provider_from_token(header=self.request.META)
        serializer = FieldWorkSerializer(data = request.data, context={"assignee": request.data.get("assignee")})
        if serializer.is_valid(raise_exception=True):
            serializer.save(provider = provider)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request,  pk):
        # provider = get_provider_from_token(header=self.request.META)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)        
        self.perform_update(serializer)
        return Response(serializer.data)

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
                return Response(data={"token":json.dumps(str(token))}, status=status.HTTP_200_OK)
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
        if check_token_validation(header=request.META):
            return Response(data={"error":"No token provided, proceed to login or register"},status=status.HTTP_403_FORBIDDEN)

        provider = get_provider_from_token(header=request.META)
        provider_instance = Provider.objects.get(id=provider.id)
        serializer = ProviderSerializer(provider_instance)
        return Response(data={"yearJoined": serializer.data["join_date"]})


class MpesaTransactions(ViewSet):

    """mpesa transaction endpoint view"""

    authentication_classes = [TokenAuthentication]
    pagination_class = PageNumberPagination

    def list(self, request):
        if check_token_validation(header=request.META):
            return Response(data={"error":"No token provided, proceed to login or register"},status=status.HTTP_403_FORBIDDEN)
        provider = get_provider_from_token(request.META)
        queryset = MpesaTransaction.objects.filter(
            provider__serial_number=provider.serial_number
        )
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset=queryset,request=self.request)
        serializer = MpesaTransactionSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

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

class BandwidthView(ViewSet):

    def create(self, request):
        if check_token_validation(header=request.META):
            return Response(data={"error":"No token provided, proceed to login or register"},status=status.HTTP_403_FORBIDDEN)

        provider = get_provider_from_token(header=request.META)
        serializer = BandwidthSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(provider = provider)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
    def destroy(self, request):
        if check_token_validation(header=request.META):
            return Response(data={"error":"No token provided, proceed to login or register"},status=status.HTTP_403_FORBIDDEN)

        provider = get_provider_from_token(header=request.META)
        serializer = BandwidthSerializer(data=serializer.data)
        bandwidth = Bandwidth.objects.get(id=serializer.data.name)
        del bandwidth
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def list(self, request):
        if check_token_validation(header=request.META):
            return Response(data={"error":"No token provided, proceed to login or register"},status=status.HTTP_403_FORBIDDEN)

        provider = get_provider_from_token(header=request.META)
        queryset = Bandwidth.objects.filter(provider=provider.id)
        serializer = BandwidthSerializer(queryset,many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)





@method_decorator(csrf_exempt, name="dispatch")
class MpesaWebHook(View):

    """mpesa callback"""

    def post(self, request):
        save_mpesa_results(results=json.loads(request.body))
        return JsonResponse(data={"ResultCode": "0", "ResultDesc": "Success"})


class SmsWebHook(View):

    """sms callback"""

    def post(self, request):
        print(request.POST)
        pass

class EmployeeView(ViewSet):
    """staff view"""

    queryset = Employee.objects.all()

    def list(self, request):
        if check_token_validation(header=request.META):
            return Response(data={"error":"No token provided, proceed to login or register"},status=status.HTTP_403_FORBIDDEN)

        provider = get_provider_from_token(header=request.META)
        queryset = Employee.objects.filter(provider=provider)
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

    def create(self, request):
        if check_token_validation(header=request.META):
            return Response(data={"error":"No token provided, proceed to login or register"},status=status.HTTP_403_FORBIDDEN)

        provider = get_provider_from_token(header=request.META)
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(provider=provider)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        if check_token_validation(header=request.META):
            return Response(data={"error":"No token provided, proceed to login or register"},status=status.HTTP_403_FORBIDDEN)
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(employee, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def partial_update(self, request, pk=None):
        if check_token_validation(header=request.META):
            return Response(data={"error":"No token provided, proceed to login or register"},status=status.HTTP_403_FORBIDDEN)
        serializer = EmployeeSerializer(data=request.data)
        
        provider = get_provider_from_token(header=request.META)
        if serializer.is_valid(raise_exception=True):
            serializer.save(provider=provider)
        return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)




class MaterialView(ViewSet):

    def create(self, request):
        if check_token_validation(header=request.META):
            return Response(data={"error":"No token provided, proceed to login or register"},status=status.HTTP_403_FORBIDDEN)

        provider = get_provider_from_token(header=self.request.META)
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(provider=provider)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
class InventoryView(ViewSet):

    queryset = Inventory.objects.all()

    def create(self, request):
        if check_token_validation(header=request.META):
            return Response(data={"error":"No token provided, proceed to login or register"},status=status.HTTP_403_FORBIDDEN)

        provider = get_provider_from_token(header=self.request.META)
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(provider=provider)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        # return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        if check_token_validation(header=request.META):
            return Response(data={"error":"No token provided, proceed to login or register"},status=status.HTTP_403_FORBIDDEN)

        provider = get_provider_from_token(header=self.request.META)
        serializer = InventorySerializer(self.queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)        
    
    def retrieve(self, request, pk=None):

        if check_token_validation(header=request.META):
            return Response(data={"error":"No token provided, proceed to login or register"},status=status.HTTP_403_FORBIDDEN)
        
        provider = get_provider_from_token(header=self.request.META)

        try:
            inventory = Inventory.objects.get(id = pk)
        except inventory.DoesNotExist:
            return Response(data={"error": "No inventory with such an id"}, status=status.HTTP_404_NOT_FOUND)
        else: 
            serializer = InventorySerializer(instance=inventory)
            return Response(data=serializer.data, status=status.HTTP_200_OK)        
    
    def partial_update(self, request, pk=None):

        if check_token_validation(header=request.META):
            return Response(data={"error":"No token provided, proceed to login or register"},status=status.HTTP_403_FORBIDDEN)
        
        provider = get_provider_from_token(header=self.request.META)

        try:
            inventory = Inventory.objects.get(id = pk)
        except inventory.DoesNotExist:
            return Response(data={"error": "No inventory with such an id"}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = InventorySerializer(inventory, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                inventory.additional_stock += serializer.instance.additional_stock
                serializer_instance = serializer.save(provider=provider)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class SmsGatewayResponseView(ModelViewSet):

    queryset = SmsGatewayResponse.objects.all()
    

