from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from apps.work_steps.models import Work_step
from .serializers import Work_stepSerializer

class Work_stepListAPIView(ListAPIView):
    queryset = Work_step.objects.all()
    serializer_class = Work_stepSerializer

class Work_stepCreateAPIView(CreateAPIView):
    queryset = Work_step.objects.all()
    serializer_class = Work_stepSerializer

class Work_stepUpdateAPIView(UpdateAPIView):
    queryset = Work_step.objects.all()
    serializer_class = Work_stepSerializer

class Work_stepDestroyAPIView(DestroyAPIView):
    queryset = Work_step.objects.all()
    serializer_class = Work_stepSerializer