from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):

    """A model serializer for client model"""

    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = ["serial", "registration_date"]
