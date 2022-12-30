# Create your tests here.
from django.urls import *
from .views import *

urlpatterns = [
    path('application/', ApplicationListAPIView.as_view()),
    path('application/create', ApplicationCreateAPIView.as_view()),
    path('application/update/<int:pk>', ApplicationUpdateAPIView.as_view()),
    path('application/delete/<int:pk>', ApplicationDestroyAPIView.as_view()),
]