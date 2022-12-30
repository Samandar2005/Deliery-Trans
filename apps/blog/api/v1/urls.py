# Create your tests here.
from django.urls import *
from .views import *

urlpatterns = [
    path('blog/',BlogListAPIView.as_view()),
    path('blog/<int:pk>',BlogRetrieveAPIView.as_view()),
    path('blog/create', BlogCreateAPIView.as_view()),
    path('blog/update/<int:pk>', BlogUpdateAPIView.as_view()),
    path('blog/delete/<int:pk>', BlogDestroyAPIView.as_view()),
]