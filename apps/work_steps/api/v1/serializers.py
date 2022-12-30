from rest_framework import serializers
from apps.work_steps.models import Work_step


class Work_stepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Work_step
        fields = '__all__'
