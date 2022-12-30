from rest_framework import serializers
from apps.about.models import AboutCompaniy


class AboutCompaniySerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutCompaniy
        fields = '__all__'
