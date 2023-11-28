from rest_framework import serializers
from .models import Client, FieldWork, Bandwidth


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