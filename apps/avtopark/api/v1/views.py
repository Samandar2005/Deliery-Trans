from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from apps.avtopark.models import Avtopark
from .serializers import AvtoparkSerializer

class AvtoparkListAPIView(ListAPIView):
    queryset = Avtopark.objects.all()
    serializer_class = AvtoparkSerializer

class AvtoparkCreateAPIView(CreateAPIView):
    queryset = Avtopark.objects.all()
    serializer_class = AvtoparkSerializer

class AvtoparkUpdateAPIView(UpdateAPIView):
    queryset = Avtopark.objects.all()
    serializer_class = AvtoparkSerializer

class AvtoparkDestroyAPIView(DestroyAPIView):
    queryset = Avtopark.objects.all()
    serializer_class = AvtoparkSerializer