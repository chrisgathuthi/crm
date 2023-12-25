from rest_framework import serializers
from .models import Client, FieldWork, Bandwidth, ShortMessage, Provider
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class BandwidthSerializer(serializers.ModelSerializer):
    """Bandwidth class serializer class"""
    class Meta:
        model = Bandwidth
        fields = "__all__"
class ClientSerializer(serializers.ModelSerializer):

    """A model serializer for client model"""
    bandwidth = serializers.StringRelatedField()

    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = ["serial", "registration_date"]


class FieldWorkSerializer(serializers.ModelSerializer):
    """serialier class for field workd"""
    assignee = serializers.StringRelatedField()
    class Meta:
        model = FieldWork
        fields = "__all__"


class ShortMessageSerializer(serializers.ModelSerializer):
    """short message model serializer"""
    to = serializers.StringRelatedField()

    class Meta:
        model = ShortMessage
        fields = "__all__"

class ProviderSerializer(serializers.ModelSerializer):
    """provider serialiser """

    class Meta:
        model = Provider
        fields = ["serial_number", "name", "location", "phone_number", "org_email", "short_code",  "join_date", "join_date", "owner", "logo", "is_activated"]
        read_only_fields = ["owner", "serial_number"]

class UserSerializer(serializers.ModelSerializer):
    """serializer for creating new partner"""

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        # password = validated_data.pop("password")
        user = get_user_model().objects.create_user(**validated_data)
        return user


class TokenSerializer(serializers.ModelSerializer):

    """token serializer"""
    class Meta:
        model = Token
        fields = "__all__"