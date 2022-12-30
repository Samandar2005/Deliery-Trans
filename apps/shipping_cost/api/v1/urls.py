# Create your tests here.
from django.urls import *
from .views import *

urlpatterns = [
    path('shipping_cost/', Shipping_costListAPIView.as_view()),
    path('shipping_cost/create', Shipping_costCreateAPIView.as_view()),
    path('shipping_cost/update/<int:pk>', Shipping_costUpdateAPIView.as_view()),
    path('shipping_cost/delete/<int:pk>', Shipping_costDestroyAPIView.as_view()),
]