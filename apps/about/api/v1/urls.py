# Create your tests here.
from django.urls import *
from .views import *

urlpatterns = [
    path('about_companiy/', AboutCompaniyListAPIView.as_view()),
    path('about_companiy/create', AboutCompaniyCreateAPIView.as_view()),
    path('about_companiy/update/<int:pk>', AboutCompaniyUpdateAPIView.as_view()),
    path('about_companiy/delete/<int:pk>', AboutCompaniyDestroyAPIView.as_view()),
]