from rest_framework import serializers
from apps.avtopark.models import Avtopark


class AvtoparkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avtopark
        fields = '__all__'
