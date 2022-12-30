from rest_framework import serializers
from apps.shipping_cost.models import Shipping_cost


class Shipping_costSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipping_cost
        fields = '__all__'
