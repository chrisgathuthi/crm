from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .utilities import convert_iso_to_mmddyyyy
from django.db import transaction
from .models import (Bandwidth, Client, FieldWork, MpesaTransaction, Provider,
                     ShortMessage, Bandwidth, Employee, Material, SmsGatewayResponse, Inventory)


class MaterialSerializer(serializers.ModelSerializer):

    """serializer for materials"""

    class Meta:
        model = Material
        fields = "__all__"
        read_only_fields = ["provider"]


class BandwidthSerializer(serializers.ModelSerializer):
    """Bandwidth class serializer class"""

    class Meta:
        model = Bandwidth
        fields = "__all__"
        read_only_fields = ["provider"]


class ClientSerializer(serializers.ModelSerializer):

    """A model serializer for client model"""

    bandwidth = serializers.StringRelatedField()

    class Meta:
        model = Client
        fields = ["id", "serial", "full_name", "first_name", "last_name", "email", "phone_number",
                  "password", "location", "router", "bandwidth", "service_plan", "status", "registration_date"]
        read_only_fields = ["serial", "registration_date", "provider", "password", "is_paid"]

    # def to_internal_value(self, data):
    #     print("The data",data)
    #     """
    #     change string representation of bandwidth name to primary key
    #     """

    #     if "bandwidth" in data:
    #         bandwidth_name = data["bandwidth"]
    #         try:
    #             bandwidth_instance = Bandwidth.objects.get(bandwidth=bandwidth_name)
    #             data["bandwidth_name"] = bandwidth_instance.id
    #         except Bandwidth.DoesNotExist:
    #             raise serializers.ValidationError("The bandwidth is invalid")
    #     return super().to_internal_value(data)

    # def to_representation(self, instance):
    #     """change bandwidth from primary key to string value"""

    #     representation = super().to_representation(instance)
    #     representation["bandwidth"] = instance.bandwidth.name
    #     return representation


class UserSerializer(serializers.ModelSerializer):
    """serializer for creating new partner"""

    class Meta:
        model = get_user_model()
        fields = ["id","username", "email", "password", "first_name", "last_name"]
        extra_kwargs = {
            "password":{"write_only":True},
            "id":{"read_only":True}
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

class EmployeeSerializer(serializers.ModelSerializer):

    """serialize staff models"""
    employee = UserSerializer(many=False)

    class Meta:
        model = Employee
        fields = ["id", "provider", "employee", "identification_number", "job_title", "salary"]
        read_only_fields = ["provider", "id"]
    
    def create(self, validated_data):
        employee_credentials = validated_data.pop("employee")

        with transaction.atomic():
            user = get_user_model().objects.create(**employee_credentials)
            employee = Employee.objects.create(employee=user, **validated_data)
        return employee
    
    def update(self, instance, validated_data):
        
        employee_credentials = validated_data.pop("employee")

        print("what is instance", instance)

        user = instance.employee #user = employee

        for attr, value in employee_credentials.items():
            setattr(user,  attr, value)
        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance

class FieldWorkSerializer(serializers.ModelSerializer):
    """serialier class for field workd"""

    assignee = EmployeeSerializer(read_only=True)
    material = serializers.StringRelatedField()

    class Meta:
        model = FieldWork
        fields = "__all__"
        read_only_fields = ["provider"]


class FieldWorkMaterialSerializer(serializers.ModelSerializer):
    """serialier class for field workd"""

    class Meta:
        model = Material
        fields = "__all__"
        read_only_fields = ["provider"]


class ShortMessageSerializer(serializers.ModelSerializer):
    """short message model serializer"""

    to = serializers.StringRelatedField()

    class Meta:
        model = ShortMessage
        fields = ["to", "sender", "message", "schedule_time", "is_sent"]
        read_only_fields = ["provider", "timestamp"]


class ProviderSerializer(serializers.ModelSerializer):
    """provider serialiser"""

    class Meta:
        model = Provider
        fields = [
            "serial_number",
            "name",
            "location",
            "phone_number",
            "org_email",
            "short_code",
            "join_date",
            "join_date",
            "owner",
            "is_activated",
        ]
        read_only_fields = ["owner", "serial_number"]




class AuthenticationSerializer(serializers.Serializer):

    """password, username serializer"""

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class TokenSerializer(serializers.ModelSerializer):

    """token serializer"""

    class Meta:
        model = Token
        fields = "__all__"


class MpesaTransactionSerializer(serializers.ModelSerializer):

    """mpesa serializer"""

    class Meta:
        model = MpesaTransaction
        fields = [
            "id",
            "transaction_id",
            "transaction_time",
            "transaction_amount",
            "bill_ref_number",
            "phone_number",
            "full_name",
        ]

    def to_representation(self, data):
        representation = super().to_representation(data)
        representation["transaction_time"] = convert_iso_to_mmddyyyy(str(data.transaction_time))
        return representation


class ClientPhoneNumberSerializer(serializers.ModelSerializer):
    """serialize clients phone numbers to send sms"""

    class Meta:
        model = Client
        fields = ["phone_number"]


class SmsGatewayResponseSerializer(serializers.ModelSerializer):

    """serialize the responses from the gateway"""

    class Meta:
        model = SmsGatewayResponse
        fields = "__all__"

class InventorySerializer(serializers.ModelSerializer):


    """serialize the invetory objects"""
    class Meta:
        model = Inventory
        exclude = ["provider"]
        read_only_fields = ["opening_stock_date", "restocking_date"]