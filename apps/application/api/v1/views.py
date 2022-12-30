from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from apps.application.models import Application
from .serializers import ApplicationSerializer

class ApplicationListAPIView(ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationCreateAPIView(CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationUpdateAPIView(UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationDestroyAPIView(DestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer