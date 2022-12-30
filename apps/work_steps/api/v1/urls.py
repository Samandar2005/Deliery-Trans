# Create your tests here.
from django.urls import *
from .views import *

urlpatterns = [
    path('work_step/', Work_stepListAPIView.as_view()),
    path('work_step/create', Work_stepCreateAPIView.as_view()),
    path('work_step/update/<int:pk>', Work_stepUpdateAPIView.as_view()),
    path('work_step/delete/<int:pk>', Work_stepDestroyAPIView.as_view()),
]