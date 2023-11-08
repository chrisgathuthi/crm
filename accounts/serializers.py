from rest_framework import serializers
from .models import Client, FieldWork


class ClientSerializer(serializers.ModelSerializer):

    """A model serializer for client model"""

    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = ["serial", "registration_date"]


class FieldWorkSerializer(serializers.ModelSerializer):
    """serialier class for field workd"""

    class Meta:
        model = FieldWork
        fields = "__all__" 