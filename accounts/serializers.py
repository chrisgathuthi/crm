from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .utilities import convert_iso_to_mmddyyyy
from .models import (Bandwidth, Client, FieldWork, MpesaTransaction, Provider,
                     ShortMessage, Bandwidth, Staff, Material, SmsGatewayResponse)


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
        fields = ["id","serial", "full_name","first_name","last_name","email", "phone_number", "password", "location", "router", "bandwidth", "service_plan", "status", "registration_date"]
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

class StaffSerializer(serializers.ModelSerializer):

    """serialize staff models"""

    class Meta:
        model = Staff
        fields = "__all__"
        read_only_fields = ["provider"]

class FieldWorkSerializer(serializers.ModelSerializer):
    """serialier class for field workd"""

    assignee = StaffSerializer(read_only=True)
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
            "logo",
            "is_activated",
        ]
        read_only_fields = ["owner", "serial_number"]


class UserSerializer(serializers.ModelSerializer):
    """serializer for creating new partner"""

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

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