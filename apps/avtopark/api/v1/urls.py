# Create your tests here.
from django.urls import *
from .views import *

urlpatterns = [
    path('avtopark/', AvtoparkListAPIView.as_view()),
    path('avtopark/create', AvtoparkCreateAPIView.as_view()),
    path('avtopark/update/<int:pk>', AvtoparkUpdateAPIView.as_view()),
    path('avtopark/delete/<int:pk>', AvtoparkDestroyAPIView.as_view()),
]