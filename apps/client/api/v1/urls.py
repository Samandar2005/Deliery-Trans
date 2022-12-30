# Create your tests here.
from django.urls import *
from .views import *

urlpatterns = [
    path('client/',ClientListAPIView.as_view()),
    path('client/create', ClientCreateAPIView.as_view()),
    path('client/update/<int:pk>', ClientUpdateAPIView.as_view()),
    path('client/delete/<int:pk>', ClientDestroyAPIView.as_view()),
]