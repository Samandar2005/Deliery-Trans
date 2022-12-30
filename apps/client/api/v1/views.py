from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from apps.client.models import Client
from .serializers import ClientSerializer

class ClientListAPIView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientCreateAPIView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientUpdateAPIView(UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDestroyAPIView(DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer