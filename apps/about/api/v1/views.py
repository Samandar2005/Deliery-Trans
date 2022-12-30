from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from apps.about.models import AboutCompaniy
from .serializers import AboutCompaniySerializer

class AboutCompaniyListAPIView(ListAPIView):
    queryset = AboutCompaniy.objects.all()
    serializer_class = AboutCompaniySerializer

class AboutCompaniyCreateAPIView(CreateAPIView):
    queryset = AboutCompaniy.objects.all()
    serializer_class = AboutCompaniySerializer

class AboutCompaniyUpdateAPIView(UpdateAPIView):
    queryset = AboutCompaniy.objects.all()
    serializer_class = AboutCompaniySerializer

class AboutCompaniyDestroyAPIView(DestroyAPIView):
    queryset = AboutCompaniy.objects.all()
    serializer_class = AboutCompaniySerializer