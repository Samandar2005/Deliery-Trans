from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from apps.shipping_cost.models import Shipping_cost
from .serializers import Shipping_costSerializer

class Shipping_costListAPIView(ListAPIView):
    queryset = Shipping_cost.objects.all()
    serializer_class = Shipping_costSerializer

class Shipping_costCreateAPIView(CreateAPIView):
    queryset = Shipping_cost.objects.all()
    serializer_class = Shipping_costSerializer

class Shipping_costUpdateAPIView(UpdateAPIView):
    queryset = Shipping_cost.objects.all()
    serializer_class = Shipping_costSerializer

class Shipping_costDestroyAPIView(DestroyAPIView):
    queryset = Shipping_cost.objects.all()
    serializer_class = Shipping_costSerializer