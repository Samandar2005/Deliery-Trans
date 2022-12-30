from rest_framework import serializers
from apps.transport.models import Transport


class TransportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transport
        fields = '__all__'
