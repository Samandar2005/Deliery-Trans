# Create your tests here.
from django.urls import *
from .views import *

urlpatterns = [
    path('transport/', TransportListAPIView.as_view()),
    path('transport/create', TransportCreateAPIView.as_view()),
    path('transport/update/<int:pk>', TransportUpdateAPIView.as_view()),
    path('transport/delete/<int:pk>', TransportDestroyAPIView.as_view()),
]