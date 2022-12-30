from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from apps.transport.models import Transport
from .serializers import TransportSerializer

class TransportListAPIView(ListAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

class TransportCreateAPIView(CreateAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

class TransportUpdateAPIView(UpdateAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

class TransportDestroyAPIView(DestroyAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer